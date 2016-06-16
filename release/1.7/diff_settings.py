BASE_DIR = '.'  ###
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'AUTOCOMMIT': True, 'ATOMIC_REQUESTS': False, 'NAME': './db.sqlite3', 'CONN_MAX_AGE': 0, 'TIME_ZONE': 'UTC', 'PORT': '', 'HOST': '', 'USER': '', 'TEST': {'COLLATION': None, 'CHARSET': None, 'NAME': None, 'MIRROR': None}, 'PASSWORD': '', 'OPTIONS': {}}}
DEBUG = True
INSTALLED_APPS = ('django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles')
MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware')
ROOT_URLCONF = 'project.urls'  ###
SECRET_KEY = '01234567890123456789012345678901234567890123456789'
SETTINGS_MODULE = 'project.settings'  ###
STATIC_URL = '/static/'
TEMPLATE_DEBUG = True
TIME_ZONE = 'UTC'
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'project.wsgi.application'