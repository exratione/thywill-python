'''
thywill django settings. Pulls in some information from the general thywill configuration.
'''

#------------------------------------------------------
# START additions to standard django settings layout
#------------------------------------------------------

from thywill_server.client_interface.client_interface_component import ClientInterfaceComponent
from thywill_server.database.database_component import DatabaseComponent
from thywill_server.database.mysql.component import MysqlComponent

django_component = ClientInterfaceComponent.factory()
database_component = DatabaseComponent.factory()

def get_database_engine():
    if( isinstance(database_component, MysqlComponent) ):
        return 'django.db.backends.mysql';
    else:
        raise NotImplementedError('Unsupported database engine in Django component settings.');



#------------------------------------------------------
# END additions to standard django settings layout
#------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': get_database_engine(),             # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': database_component.database,         # Or path to database file if using sqlite3.
        'USER': database_component.user,             # Not used with sqlite3.
        'PASSWORD': database_component.password,     # Not used with sqlite3.
        'HOST': database_component.host,             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': database_component.port,             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = django_component.secret_key

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'thywill_server.client_interface.django.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    django_component.template_path,
)

INSTALLED_APPS = (
    'django.contrib.sessions',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
