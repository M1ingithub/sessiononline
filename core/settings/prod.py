import os, environ
from core.settings.settings import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'asd'

# load production server from .env
ALLOWED_HOSTS        = [
    'localhost',
    'localhost:5432',
    '127.0.0.1',
    '162.254.34.158',
    '.session.online',
    
    env('SERVER', default='127.0.0.1')
]

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'apps/static'),
)

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', 'apps/static/assets') 

#############################################################
#############################################################

print(ASSETS_ROOT)