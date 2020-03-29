from rss_server.settings.base import *


ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR)
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
