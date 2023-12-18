"""
Django settings for nomnom project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from environ import config, group, var, to_config, bool_var
from icecream import install

install()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


@config(prefix="NOM")
class AppConfig:
    @config
    class DB:
        name = var()
        host = var()
        port = var(5432, converter=int)
        user = var()
        password = var()

    @config
    class REDIS:
        host = var()
        port = var(6379, converter=int)

    debug = bool_var(default=False)
    db = group(DB)
    redis = group(REDIS)

    @config
    class OAUTH:
        key = var()
        secret = var()

    oauth = group(OAUTH)

    secret_key = var()

    static_file_root = var(BASE_DIR / "staticfiles")


cfg = to_config(AppConfig)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cfg.secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = cfg.debug
TEMPLATE_DEBUG = cfg.debug


class InvalidStringShowWarning(str):
    def __mod__(self, other):
        import logging

        logger = logging.getLogger(__name__)
        logger.warning(
            f"In template, undefined variable or unknown value for: '{other}'"
        )
        return ""

    def __bool__(self):  # if using Python 2, use __nonzero__ instead
        # make the template tag `default` use its fallback value
        return False


ALLOWED_HOSTS = [
    "localhost",
    "void.camel-tortoise.ts.net",
    "void",
]

CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in ALLOWED_HOSTS]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # use whitenoise to serve static files, instead of django's builtin
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django_celery_results",
    "django_celery_beat",
    "django_extensions",
    "markdownify.apps.MarkdownifyConfig",
    "nominate",
    "social_django",
    "django_browser_reload",
    "django_bootstrap5",
    "fontawesomefree",
    "wsfs",
]

AUTHENTICATION_BACKENDS = [
    "nomnom.social_core.ClydeStagingOAuth2",
    # Uncomment following if you want to access the admin
    "django.contrib.auth.backends.ModelBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "nomnom.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "string_if_invalid": InvalidStringShowWarning("%s"),
        },
    },
]

WSGI_APPLICATION = "nomnom.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": cfg.db.name,
        "USER": cfg.db.user,
        "PASSWORD": cfg.db.password,
        "HOST": cfg.db.host,
        "PORT": str(cfg.db.port),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{cfg.redis.host}:{cfg.redis.port}",
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "wsfs.NomNomUser"
LOGOUT_REDIRECT_URL = "election-index"

# we are using postgres, so this is recommended in the docs.
SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIAL_AUTH_CLYDE_KEY = cfg.oauth.key
SOCIAL_AUTH_CLYDE_SECRET = cfg.oauth.secret

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = cfg.static_file_root

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "default"
CELERY_BROKER_URL = f"redis://{cfg.redis.host}:{cfg.redis.port}"
CELERY_TIMEZONE = "America/Los_Angeles"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
