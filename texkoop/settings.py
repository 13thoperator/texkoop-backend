"""
Django settings for texkoop project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.up.railway.app']


# Application definition

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'api.apps.ApiConfig',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'rest_framework',
    'cloudinary_storage',
    'cloudinary',

]
SITE_ID =1
X_FRAME_OPTIONS = 'SAMEORIGIN'
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'texkoop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'texkoop.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE':10

}
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases



if os.environ['ENVIRONMENT'] == "DEVELOPMENT":
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
else:
    DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'HOST': os.environ['PGHOST'],
        'NAME': os.environ['PGDATABASE'],
        'USER': os.environ['PGUSER'],
        'PASSWORD': os.environ['PGPASSWORD'],
        'PORT': os.environ['PGPORT'],

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




# Additional configuration settings


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#cloudinary config
CLOUDINARY_STORAGE = {
    'CLOUD_NAME' : os.environ['CLOUD_NAME'],
    'API_KEY' : os.environ['CLOUD_API_KEY'],
    'API_SECRET' : os.environ['CLOUD_API_SECRET']
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
if os.environ['ENVIRONMENT'] == "PRODUCTION":
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CORS_ORIGIN_WHITELIST = [
    f"{os.environ['FRONTEND_URL']}"
    

]

CSRF_TRUSTED_ORIGINS = ['https://backend-texkoop.up.railway.app','https://*.127.0.0.1']

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'codeSnippet_theme': 'railscasts',
        # 'toolbarCanCollapse':'true',
        'height': 420,
        'width': "auto",
        'extraPlugins': ','.join(
            [
                'dialog', 'autolink',


            ]),
    },

}



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
