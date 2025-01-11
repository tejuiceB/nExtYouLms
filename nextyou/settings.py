from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Cloudinary Imports
import cloudinary
import cloudinary.uploader
import cloudinary.api

from decouple import Config, Csv
from pathlib import Path

# Initialize the Config object and explicitly specify the .env file location
config = Config('.env')  # Assumes the .env file is in the same directory as your settings.py

# Use environment variable for Cloudinary URL
CLOUDINARY_URL = config('CLOUDINARY_URL', default='cloudinary://414785722153739:DfULH9yUdP3Q2UoORgzNt-M_F5E@duddm6g7q')


# Now use the parsed URL to configure Cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_URL.split('@')[1],
    api_key=CLOUDINARY_URL.split(':')[1].split('@')[0],
    api_secret=CLOUDINARY_URL.split(':')[2].split('@')[0],
)

cloudinary.config( 
    cloud_name = "duddm6g7q", 
    api_key = "414785722153739", 
    api_secret = "DfULH9yUdP3Q2UoORgzNt-M_F5E", # Click 'View API Keys' above to copy your API secret
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&dgr^x)^#^jnys&p9g7djz&vd$1##vz3(c@1fbb3!c6yd^#f-#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change this to True for local development

ALLOWED_HOSTS = ["nextyou.up.railway.app", "127.0.0.1", "localhost"]  # Added localhost and 127.0.0.1

CSRF_TRUSTED_ORIGINS = []  # Commented this out for local development

CORS_ORIGIN_WHITELIST = [
    'https://nextyou.up.railway.app'
]

CORS_ORIGIN_ALLOW_ALL = True  # Allow all origins during local development

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'allauth',

    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'cloudinary',

    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nextyou.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '477770344081-i7ohji3vs341dbf06vo74eftglnbfes4.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}


# django-allauth registration settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

# 1 day
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400

# or any other page
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# ACCOUNT_EMAIL_VERIFICATION = "none"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

WSGI_APPLICATION = 'nextyou.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tejuice',
        'USER': 'teju',
        'PASSWORD': '7889',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = 'unknownuser7825@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'unknownuser7825@gmail.com'
EMAIL_HOST_PASSWORD = 'vzmn zujk rxqr yiqb'  # Make sure this is correct

# Cloudinary Django Integration

cloudinary.config(
    cloud_name='dw7whhgws',
    api_key='277146194325425',
    api_secret='Z4Y0f8yvo7lRkK2Is1yaOLcJJeo',
)