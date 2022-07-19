from timetable.settings.base import *
import os, dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', None)

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES['default'] = dj_database_url.parse(
    url=os.getenv('DATABASE_URL'), conn_max_age=600
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'timetable/assets',
]


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'