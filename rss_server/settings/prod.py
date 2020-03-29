from rss_server.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rss_db',
        'USER': 'zuck3rb3rg@zuck3rb3rg',
        'PASSWORD': '2DyPo5My2X51',
        'HOST': 'zuck3rb3rg.mysql.database.azure.com',
        'PORT': '3306'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

# STATIC_ROOT = os.path.join(BASE_DIR)
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

