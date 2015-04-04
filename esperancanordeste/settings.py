# coding: utf-8
"""
Django settings for esperancanordeste project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.localhost',
     '127.0.0.1',
     '.herokuapp.com',
     '.esperancanordeste.com.br',
     '.ow7.com.br'
]


# Application definition

INSTALLED_APPS = (
    'grappelli_extensions',
    'grappelli.dashboard',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # other apps
    'south',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'taggit',
    'embed_video',

    # my apps
    'esperancanordeste.core',
    'esperancanordeste.catalog',
    'esperancanordeste.campain',
    'esperancanordeste.sale',
    'esperancanordeste.newsletter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'esperancanordeste.current_user.CurrentUserMiddleware',
)

ROOT_URLCONF = 'esperancanordeste.urls'

WSGI_APPLICATION = 'esperancanordeste.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEFAULT_FROM_EMAIL = 'Esperança Nordeste <no-reply@esperancanordeste.com.br>'
# EMAIL_USE_TLS = True
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587


# django-tinymce
# TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'theme_advanced_buttons1': "cut,copy,paste,|,undo,redo,|,cleanup,|,bold,\
                                italic,underline,strikethrough,|,forecolor,\
                                backcolor,|,justifyleft,justifycenter,\
                                justifyright,justifyfull,|,help,|,code",
    'theme_advanced_buttons2': "removeformat,formatselect,fontsizeselect,|,\
                                bullist,numlist,outdent,indent,|,link,unlink,\
                                anchor,sub,sup,|,hr,advhr,visualaid,|,image,\
                                media,|,preview,",
    'height': '350',
    'file_browser_callback': 'mce_filebrowser',
}


# grappelli
GRAPPELLI_ADMIN_TITLE = 'OW7 | CMS'

GRAPPELLI_EXTENSIONS_NAVBAR = 'esperancanordeste.extensions.Navbar'

GRAPPELLI_EXTENSIONS_SIDEBAR = 'esperancanordeste.extensions.Sidebar'

GRAPPELLI_INDEX_DASHBOARD = 'esperancanordeste.dashboard.CustomIndexDashboard'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)


# south {taggit}
SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
    'photologue': 'photologue.south_migrations',
}
