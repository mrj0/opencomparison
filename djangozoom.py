import logging 

DATABASES = {
    "default": {
        "ENGINE": "postgresql_psycopg2", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "opencomparison",          # Or path to database file if using sqlite3.
        "USER": "audreyr",              # Not used with sqlite3.
        "PASSWORD": "",                  # Not used with sqlite3.
        "HOST": "localhost",             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "5432",                  # Set to empty string for default. Not used with sqlite3.
    }
}


DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG
#TEST_RUNNER = 'testrunner.OurTestRunner'

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s "%(message)s" in %(funcName)s() line %(lineno)d in %(pathname)s', 
        filename='main.log',
        filemode='a',
)

LOCAL_INSTALLED_APPS = []

LAUNCHPAD_ACTIVE = False

# Analytics ID
URCHIN_ID = ""

# Email Settings
DEFAULT_FROM_EMAIL = \
        'Django Packages <djangopackages-noreply@djangopackages.com>'
EMAIL_SUBJECT_PREFIX = '[Django Packages] '

# Make this unique, and don't share it with anybody.
SECRET_KEY = "eangkwet-3to3nf-agw43-KFNDS#-3gegshg4-rgw43KLJdf"

# You can remove this after you change your SECRET_KEY
if SECRET_KEY == "CHANGE-THIS-KEY-TO-SOMETHING-ELSE":
    raise Exception('You must change your SECRET_KEY settings in '
            'local_settings.py.')

# See http://celeryproject.org/docs/configuration.html#task-execution-settings
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = "django"

LOCAL_INSTALLED_APPS = ('djkombu', )