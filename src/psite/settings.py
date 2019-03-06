"""
Django settings for psite project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mennahaircare@gmail.com'
EMAIL_HOST_PASSWORD = 'menn@h@irkare'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ol_sgvi-ip5jrsj%($p-r2r&p7um17h$d&&a!hcr_gqc&cneyw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profiles',
    'contact',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'checkout',
    'stripe',
    'payments'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'psite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
WSGI_APPLICATION = 'psite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# media dir will be used to holed user gen. content such as images
# static dir for js and css



# we are gonna set some dir path when debug = true
# debug will be true only on dev
# we need to change it when the site is live
if DEBUG:
    MEDIA_URL ='/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static", "static"), 
        )
CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

LOGIN_URL = '/accounts/login/' # login page
LOGIN_REDIRECT_URL = '/' # go to after loging in to home page


ACCOUNT_AUTHENTICATION_METHOD = 'username_email' 
ACCOUNT_CONFIRM_EMAIL_ON_GET = False # when the user account is all auth will look when the user accsess is confiremed
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL # when the user sign up and get confirmed email msg , will be redirected to login page 
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None # redirect signed in user to home page

ACCOUT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3 # when the confirm msg link expire
ACCOUNT_EMAIL_REQUIRED = False # user can reg with just username and pw
ACCOUNT_EMAIL_VERIFICATION = None # allow login with unverfieed mail
ACCOUNT_EMAIL_SUBJECT_PREFIX = "My subject:" # sdefault subject
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http" 

ACCOUNT_LOGOUT_ON_GET = False # logout confirmation dialog
ACCOUNT_LOGOUT_REDIRECT_URL = "/"  # go to when being logout to home
ACCOUNT_SIGNUP_FORM_CLASS = None # 
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True # password verfication
ACOUNT_UNIQUE_EMAIL = True # no 2 acc with the same mail
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username" # set the name of the field
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH = 5 # min length duuh ?
ACCOUNT_USERNAME_BLACKLIST = [] # blocked usernames
ACCOUNT_USERNAME_REQUIRED = True # username must be entred when signing up
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False # password will be hidden when the user type
ACCOUNT_PASSWORD_MIN_LENGTH = 6 # min pw length duuh ?
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True # Auto login when signing uo


PAYMENT_HOST = 'localhost:8000'
PAYMENT_USES_SSL = True
PAYMENT_MODEL = 'paymentapp.Payment'
PAYMENT_VARIANTS = {
    'default': ('payments.dummy.DummyProvider', {})}