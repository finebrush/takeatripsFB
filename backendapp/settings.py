"""
Django settings for test_app project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8fkupu8pa%%u$wgk6c!os39el41v7i7^u*8xs3@~]$asffw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '.takeatrips.com',
    '15.164.63.68',
]

# Application definition

INSTALLED_APPS = [
    'vali',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',

    'taggit',
    'leaflet',
    'dal',
    'dal_select2',
    'mapwidgets',
    'smart_selects',
    'fieldsets_with_inlines',
    # allauth 등록
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # provider 구글, 페이스북, 카톡, 깃허브 등 소셜로그인 제공 업체
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    'import_export',
    'rest_framework',
    'django_filters',
    'django_summernote',

    'backendapp.travels',
    'backendapp.common',
    'backendapp.arcontent',
    'clientapp',
    'blogapp.apps.BlogappConfig',
    'accounts.apps.AccountsConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': {
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             }
#         },
#     },
# ]

ROOT_URLCONF = 'backendapp.urls'

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

# For backwards compatibility with Django 1.8
# MIDDLEWARE_CLASSES = MIDDLEWARE

WSGI_APPLICATION = 'backendapp.wsgi.application'

VALI_CONFIG = {
    # the vali-admin themes  default, blue, purple, green,brown
    'theme': 'default',
    'dashboard': {
        'name': 'Dashboard',
        'url': '/admin/dashboard/',
        'subtitle': 'Dashboard view with all statistics',
        'site_name': 'Dashboard admin',
        'url_image_profile': ''
    },
    'fieldset': {
        'fields': ['user_permissions', 'permissions']
    },
    # the order for applist  default, registry
    # display applist by group: True
    #  e.g. {group: True}
    # default check decorators  vali.decorator.vali_models_group on ModelAdmin
    #  * otherwize use group_marker in verbose_name_plural, (will be deprecated in future version 0.2.0)*
    #  * e.g.  {group: True, group_marker : '-'}
    #    verbose_name_plural = system-user
    #  * display the model "user" in group "system"
    'applist': {
        'order': "registry", "group": True
    }
}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#-----local Test -------
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'takebo', #Name of the database
        'USER': 'finebrush', #Name of the user
        'HOST': 'localhost', #Change if the database lives in a system different from your local system. 'PASSWORD': 'xxxxxxx',
        'PORT': '5432',
    }
}

# -------amazon DB ---------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'HOST': 'takeatrips.cee1z1owr2pr.ap-northeast-2.rds.amazonaws.com',
#         'PORT': '5432',
#         'NAME': 'takeatrips',
#         'USER': 'takebo',
#         'PASSWORD': 'anfruf88',
#     }
# }

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 11),
        ("mapCenterLocation", [37.59675, 126.99488]),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyA9P6UvbrGzl1-ooprZXq4HghPXX27Q7Po"
}

# LEAFLET_CONFIG = {
#     'SPATIAL_EXTENT': (123.41144, 38.96579, 132.28839, 32.75722), # 이 범위 안에서만 드래그 이동이 됨..
#     'DEFAULT_CENTER': (52.00, 20.00), # (-.023, 36.87),
#     'DEFAULT_ZOOM': 8,
#     'MAX_ZOOM': 20,
#     'MIN_ZOOM':3,
#     'SCALE': 'both',
#     'ATTRIBUTION_PREFIX': 'Inspired by Life in Takeatrips'
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

SITE_ID = 1
LOGIN_REDIRECT_URL = '/' # 로그인 후 또는 오류가 났을 때 루트로 이동

USE_DJANGO_JQUERY = False
JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ko'
# LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('ko', _('Korean')),
    ('en', _('English')),
    ('vi', _('Vietnamese')),
]

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
	os.path.join(BASE_DIR, 'locale'),
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")