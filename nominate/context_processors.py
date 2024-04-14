from urllib.parse import urlparse

from django.conf import settings
from django.templatetags.static import static
from django_svcs.apps import svcs_from
from nomnom.convention import ConventionConfiguration

from nominate import models


def site(request):
    convention = svcs_from(request).get(ConventionConfiguration)

    admin_message_obj = models.AdminMessage.objects.filter(active=True).first()
    if admin_message_obj is not None:
        admin_message = admin_message_obj.message
    else:
        admin_message = None

    return {
        "USERNAME_LOGIN": settings.NOMNOM_ALLOW_USERNAME_LOGIN_FOR_MEMBERS,
        "HUGO_HELP_EMAIL": convention.get_hugo_help_email(request),
        "REGISTRATION_EMAIL": convention.get_registration_email(request),
        "CONVENTION_NAME": convention.name,
        "CONVENTION_SUBTITLE": convention.subtitle,
        "CONVENTION_SLUG": convention.slug,
        "CONVENTION_SITE_URL": convention.site_url,
        "CONVENTION_LOGO_ALT_TEXT": convention.logo_alt_text,
        "CONVENTION_LOGO": url_or_static(convention.logo),
        "ADMIN_MESSAGE": admin_message,
    }


def url_or_static(url: str) -> str:
    urlparts = urlparse(url)
    if bool(urlparts.scheme):
        return url
    return static(url)
