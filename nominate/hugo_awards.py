from collections import defaultdict
from dataclasses import dataclass, field
from io import StringIO
from itertools import takewhile
from operator import itemgetter

import pyrankvote
from django.utils.safestring import mark_safe
from pyrankvote.helpers import (
    CandidateStatus,
    ElectionResults,
    RoundResult,
)

from nominate import models
from nomnom.convention import HugoAwards
from wsfs.rules.constitution_2023 import ElectionBallots, ballots_from_category


def get_winners_for_election(
    awards: HugoAwards, election: models.Election
) -> dict[models.Category, ElectionResults]:
    category_results: dict[models.Category, ElectionResults] = {}
    for c in election.category_set.all():
        category_results[c] = run_election(awards, c)

    return category_results


def run_election(
    awards: HugoAwards,
    category: models.Category,
    excluded_finalists: list[models.Finalist] | None = None,
) -> ElectionResults:
    election_ballots = ballots_from_category(
        category, excluded_finalists=excluded_finalists
    )

    return run_election_with_ballots(awards, category, election_ballots)


def run_election_with_ballots(
    awards: HugoAwards, category: models.Category, election_ballots: ElectionBallots
) -> ElectionResults:
    maybe_no_award = [c for c in category.finalist_set.all() if c.name == "No Award"]
    if maybe_no_award:
        no_award = pyrankvote.Candidate(str(maybe_no_award[0]))
    else:
        no_award = None

    return awards.counter(
        ballots=election_ballots.ballots,
        candidates=election_ballots.candidates,
        runoff_candidate=no_award,
    )


@dataclass
class VPR:
    votes: str | None
    eliminated: bool = False
    winner: bool = False
    won: bool = False

    def __str__(self):
        return self.votes if self.votes else mark_safe("&nbsp;")

    @property
    def extra_class(self) -> str:
        class_list = []
        if self.winner:
            class_list.append("winner")

        if self.eliminated:
            class_list.append("eliminated")

        if self.won:
            class_list.append("won")

        return " ".join(class_list)

    @property
    def is_empty(self) -> bool:
        return self.votes is None


@dataclass
class CandidateResults:
    candidate: str
    votes_per_round: list[float | None] = field(default_factory=list)
    won: bool = False

    @property
    def float_format(self) -> str:
        all_integers = all(v is None or v.is_integer() for v in self.votes_per_round)
        return ".0f" if all_integers else ".2f"

    def votes_per_round_details(self) -> list[VPR]:
        return [
            VPR(
                votes=f"{v:{self.float_format}}" if v is not None else None,
                eliminated=(
                    not self.won
                    and (i == self.rounds - 1 or i == len(self.votes_per_round) - 1)
                ),
                winner=self.won,
                won=self.won and i >= len(self.votes_per_round) - 2,
            )
            for i, v in enumerate(self.votes_per_round)
        ]

    @property
    def rounds(self) -> int:
        # the only votes we count are all the votes in votes_per_round before the first None value
        valid_votes = list(takewhile(lambda x: x is not None, self.votes_per_round))
        return len(valid_votes)

    @property
    def sort_key(self) -> int:
        # bump up the winner a bit
        if self.won and self.candidate != "No Award":
            return self.rounds + 1
        return self.rounds


class SlantTable:
    def __init__(self, results: list[RoundResult], title: str):
        self.results = results
        self.title = title

        self.process_rounds()

    def to_html(self) -> str:
        return mark_safe(self.to_html_table())

    def to_html_table(self) -> str:
        io = StringIO()
        io.write(f"<tr>{self._header()}</tr>")

        for candidate_name in self.candidate_order:
            if candidate_name in self.winners:
                io.write('<tr class="winner">')
            else:
                io.write("<tr>")
            io.write(f"<td>{candidate_name}</td>")

            eliminated = False

            for round_index, result in enumerate(self.results):
                candidate_result = next(
                    (
                        cr
                        for cr in result.candidate_results
                        if cr.candidate.name == candidate_name
                    ),
                    None,
                )

                if (
                    eliminated
                    and candidate_result
                    and candidate_result.number_of_votes == 0.0
                ):
                    io.write('<td class="blank">&nbsp;</td>')
                    continue

                if candidate_result:
                    if candidate_result.status == CandidateStatus.Elected:
                        io.write(
                            f'<td class="won">{candidate_result.number_of_votes:.0f}</td>'
                        )
                    elif candidate_result.status == CandidateStatus.Rejected:
                        io.write(
                            f'<td class="eliminated">{candidate_result.number_of_votes:.0f}</td>'
                        )
                        eliminated = True

                    else:
                        io.write(f"<td>{candidate_result.number_of_votes:.0f}</td>")
                else:
                    io.write('<td class="blank">&nbsp;</td>')

            io.write("</tr>")

        return f'<table class="results">{io.getvalue()}</table>'

    def _header(self) -> str:
        return f"<th colspan='{len(self.results)}'>{self.title}</th><th>Runoff</th>"

    def process_rounds(self) -> None:
        """
        Process the round results to determine the survival status of each candidate
        in each round.
        """
        self.winners = []

        candidate_survival = defaultdict(int)

        # we ignore the last round of results; that's a runoff round and all of our
        # candidates will be seen before then.
        already_rejected = set()

        for round_index, round_result in enumerate(self.results[:-1]):
            for candidate_result in round_result.candidate_results:
                if candidate_result.status == CandidateStatus.Rejected:
                    if candidate_result.candidate.name not in already_rejected:
                        already_rejected.add(candidate_result.candidate.name)
                        candidate_survival[candidate_result.candidate.name] = (
                            round_index
                        )

                else:
                    candidate_survival[candidate_result.candidate.name] = round_index
                    if candidate_result.status == CandidateStatus.Elected:
                        self.winners.append(candidate_result.candidate.name)

        # Sort candidates by the number of rounds they survived, elected candidates first.
        sorted_candidates = reversed(
            sorted(candidate_survival.items(), key=itemgetter(1))
        )
        sorted_candidates = [c for c, _ in sorted_candidates]

        self.candidate_order = sorted_candidates
