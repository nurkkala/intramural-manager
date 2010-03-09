# Django settings for intramurals project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    # ('aubrown', 'agustinmichaelbrown@gmail.com'),
)

MANAGERS = ADMINS

from os.path import abspath, dirname
print (dirname(abspath(__file__)) + '/sandbox.py')

"""Description: Matches US phone number format. 1 in the beginning is optional, area code is required, spaces or dashes can be used as optional divider between number groups. Also alphanumeric format is allowed after area code. Also, accepts campust phone numbers of 4 or 5 digits
Matches: 1-(123)-123-1234 | 123 123 1234 | 1-800-ALPHNUM | 85555
Non-Matches: 1.123.123.1234 | (123)-1234-123 | 123-1234"""

PHONE_REGEX = r'^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})|\d{4,5}$'  

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '' #'intramurlsApp/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://cse.taylor.edu/~cos372f0901/intramurals/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!mpp(x97zy8y1xz#@25zbeekd@1x1@y$=-ugppgn*ly=wb3c=k'

#email settings
EMAIL_HOST = 'smtp.cse.taylor.edu'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'intramuralsApp',
)

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json',
}
