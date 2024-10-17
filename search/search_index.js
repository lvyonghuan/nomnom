var __index = {"config":{"lang":["en"],"separator":"[\\s\\-]+","pipeline":["stopWordFilter"]},"docs":[{"location":"index.html","title":"Nom Nom (nom)","text":""},{"location":"code_of_conduct.html","title":"Contributor Covenant Code of Conduct","text":""},{"location":"code_of_conduct.html#our-pledge","title":"Our Pledge","text":"<p>We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, caste, color, religion, or sexual identity and orientation.</p> <p>We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.</p>"},{"location":"code_of_conduct.html#our-standards","title":"Our Standards","text":"<p>Examples of behavior that contributes to a positive environment for our community include:</p> <ul> <li>Demonstrating empathy and kindness toward other people</li> <li>Being respectful of differing opinions, viewpoints, and experiences</li> <li>Giving and gracefully accepting constructive feedback</li> <li>Accepting responsibility and apologizing to those affected by our mistakes,   and learning from the experience</li> <li>Focusing on what is best not just for us as individuals, but for the overall   community</li> </ul> <p>Examples of unacceptable behavior include:</p> <ul> <li>The use of sexualized language or imagery, and sexual attention or advances of   any kind</li> <li>Trolling, insulting or derogatory comments, and personal or political attacks</li> <li>Public or private harassment</li> <li>Publishing others' private information, such as a physical or email address,   without their explicit permission</li> <li>Other conduct which could reasonably be considered inappropriate in a   professional setting</li> </ul>"},{"location":"code_of_conduct.html#enforcement-responsibilities","title":"Enforcement Responsibilities","text":"<p>Community leaders are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem inappropriate, threatening, offensive, or harmful.</p> <p>Community leaders have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, and will communicate reasons for moderation decisions when appropriate.</p>"},{"location":"code_of_conduct.html#scope","title":"Scope","text":"<p>This Code of Conduct applies within all community spaces, and also applies when an individual is officially representing the community in public spaces. Examples of representing our community include using an official email address, posting via an official social media account, or acting as an appointed representative at an online or offline event.</p>"},{"location":"code_of_conduct.html#enforcement","title":"Enforcement","text":"<p>Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the community leaders responsible for enforcement at offline@offby1.net. All complaints will be reviewed and investigated promptly and fairly.</p> <p>All community leaders are obligated to respect the privacy and security of the reporter of any incident.</p>"},{"location":"code_of_conduct.html#enforcement-guidelines","title":"Enforcement Guidelines","text":"<p>Community leaders will follow these Community Impact Guidelines in determining the consequences for any action they deem in violation of this Code of Conduct:</p>"},{"location":"code_of_conduct.html#1-correction","title":"1. Correction","text":"<p>Community Impact: Use of inappropriate language or other behavior deemed unprofessional or unwelcome in the community.</p> <p>Consequence: A private, written warning from community leaders, providing clarity around the nature of the violation and an explanation of why the behavior was inappropriate. A public apology may be requested.</p>"},{"location":"code_of_conduct.html#2-warning","title":"2. Warning","text":"<p>Community Impact: A violation through a single incident or series of actions.</p> <p>Consequence: A warning with consequences for continued behavior. No interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, for a specified period of time. This includes avoiding interactions in community spaces as well as external channels like social media. Violating these terms may lead to a temporary or permanent ban.</p>"},{"location":"code_of_conduct.html#3-temporary-ban","title":"3. Temporary Ban","text":"<p>Community Impact: A serious violation of community standards, including sustained inappropriate behavior.</p> <p>Consequence: A temporary ban from any sort of interaction or public communication with the community for a specified period of time. No public or private interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, is allowed during this period. Violating these terms may lead to a permanent ban.</p>"},{"location":"code_of_conduct.html#4-permanent-ban","title":"4. Permanent Ban","text":"<p>Community Impact: Demonstrating a pattern of violation of community standards, including sustained inappropriate behavior, harassment of an individual, or aggression toward or disparagement of classes of individuals.</p> <p>Consequence: A permanent ban from any sort of public interaction within the community.</p>"},{"location":"code_of_conduct.html#attribution","title":"Attribution","text":"<p>This Code of Conduct is adapted from the Contributor Covenant, version 2.1, available at https://www.contributor-covenant.org/version/2/1/code_of_conduct.html.</p> <p>Community Impact Guidelines were inspired by Mozilla's code of conduct enforcement ladder.</p> <p>For answers to common questions about this code of conduct, see the FAQ at https://www.contributor-covenant.org/faq. Translations are available at https://www.contributor-covenant.org/translations.</p>"},{"location":"admin/advisory_votes.html","title":"Advisory Votes","text":"<p>This is an optional feature added to support Glasgow 2024's \"Advisory Vote\" concept.</p>"},{"location":"admin/advisory_votes.html#creating-a-new-vote","title":"Creating a new Vote","text":"<p>Votes are created in the admin pages, located at <code>/admin/advise/proposal/</code></p> <p>The detail page offers a title, a markdown entry for the full text of the proposal, and a couple of admin controls for it. By default, abstentions are not permitted, but that can be optionally enabled.</p> <p>The proposal will be visible at <code>/bm/&lt;id&gt;</code> to logged in WSFS members.</p>"},{"location":"admin/advisory_votes.html#permissions","title":"Permissions","text":"<p>In order to administer these, the following permissions should be set for any staff member who should be able to see it:</p> <pre><code>Advise | proposal | Can add proposal\nAdvise | proposal | Can change proposal\nAdvise | proposal | Can view proposal\nAdvise | proposal | Can delete proposal\nAdvise | vote | Can add vote\nAdvise | vote | Can change vote\nAdvise | vote | Can view vote\nAdvise | vote | Can delete vote\nAdvise | vote admin data | Can add vote admin data\nAdvise | vote admin data | Can change vote admin data\nAdvise | vote admin data | Can view vote admin data\nAdvise | vote admin data | Can delete vote admin data\n</code></pre>"},{"location":"admin/paper_ballots.html","title":"Paper Ballots","text":"<p>To handle paper ballots, the Admin can create a member record, and then manually enter their nominations.</p>"},{"location":"admin/paper_ballots.html#creating-a-member-record","title":"Creating a Member Record","text":"<p>This is accomplished in the Admin dashboard, for example /admin/nominate/nominatingmemberprofile/</p> <ol> <li>Click \"Add Nominating Member Profile\"</li> <li>Fill in the member number from the convention, and the name of the member.</li> <li>Click \"Save\"</li> </ol>"},{"location":"admin/paper_ballots.html#editing-the-ballot","title":"Editing the Ballot","text":"<p>To edit the ballot, select the member profile from the list (either by searching, listing, or in the case of one you've just created, you'll already be on that page).</p> <p>The \"Ballot Management\" section will have links to all open elections. You can choose \"Manage Nominations\" or \"Manage Votes\" from that set.</p> <p>You will be taken to the final ballot page, but in the role of the member instead of yourself. You can edit the entire ballot in place, and when you are done and save, the member's ballot will be updated.</p> <p>Info</p> <p>If the member has an email address registered in NomNom, it will be emailed the results the ballot being saved, along with a message indicating that the change was made.</p>"},{"location":"dev/index.html","title":"Index","text":""},{"location":"dev/index.html#development","title":"Development","text":"<p>Development of this system depends on you having four things installed:</p> <ul> <li>docker (with the compose addon)</li> <li>the postgresql command line tool</li> <li>python 3.12 (ideally using mise)</li> <li>pdm</li> </ul> <p>The instructions here are for macOS; where appropriate, they'll proffer a Linux equivalent.</p> <p>Info</p> <p>Regrettably, I don't develop on Windows; I would welcome Windows versions of these instructions!</p>"},{"location":"dev/index.html#install-your-dependencies","title":"Install your dependencies","text":"<p>On macOS, that means installing copier, uv, and just. For simplicity these instructions will assume that you have homebrew installed, and follow the instructions to set your PATH for each tool.</p> <ul> <li> <p> Just</p> <p>Just is a task runner; it uses a Justfile to describe steps to run, and I use it here to manage the setup and development processes.</p> <p>Install it from your package manager:</p> <pre><code>$ brew install just\n$ just --version\njust 1.16.0\n</code></pre> </li> <li> <p> Python</p> <p>\"How to install Python\" is beyond the scope of this README, sorry; I use mise but any method will work. When you have it set up, you should be able to run this code in the source directory and get something vaguely correct:</p> <pre><code>$ python3.12 --version\nPython 3.12.3\n</code></pre> </li> <li> <p> uv</p> <p>uv should be in your system package manager; on macOS that's probably homebrew:</p> <pre><code>$ brew install uv\n... lots of output\n$ uv -V\nuv 0.3.0 (dd1934c9c 2024-08-20)\n</code></pre> </li> <li> <p> Docker compose</p> <p>\"Installing docker\" is also beyond the scope here. You probably want Docker Desktop. Once it's installed, this should work:</p> <pre><code>$ docker compose ps\nNAME                IMAGE               COMMAND                  SERVICE             CREATED             STATUS              PORTS\n</code></pre> </li> </ul>"},{"location":"dev/index.html#generate-a-test-convention","title":"Generate a test convention","text":"<p>Using copier, create a new convention project:</p> <pre><code>$ uvx copier copy --trust gh:WorldconVotingSystems/nomnom &lt;your-project-dir&gt;\n</code></pre> <p>Note the <code>--trust</code> flag; that's because the template uses the <code>_tasks</code> key, which runs some postprocessing on the generated template to verify it all works.</p> <p>Feel free to check out the contents of the copier configuration to make sure it's safe.</p>"}]}