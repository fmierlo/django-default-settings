DATABASES = {'default': {'ENGINE': 'django.db.backends.', 'NAME': '', 'HOST': '', 'USER': '', 'PASSWORD': '', 'PORT': ''}}
DEBUG = True
INSTALLED_APPS = ('django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.sites', 'django.contrib.messages', 'django.contrib.staticfiles')
LOGGING = {'loggers': {'django.request': {'level': 'ERROR', 'propagate': True, 'handlers': ['mail_admins']}}, 'version': 1, 'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}}, 'disable_existing_loggers': False, 'handlers': {'mail_admins': {'class': 'django.utils.log.AdminEmailHandler', 'filters': ['require_debug_false'], 'level': 'ERROR'}}}
ROOT_URLCONF = 'project.urls'  ###
SECRET_KEY = '01234567890123456789012345678901234567890123456789'
SETTINGS_MODULE = 'project.settings'  ###
SITE_ID = 1  ###
STATIC_URL = '/static/'
TEMPLATE_DEBUG = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'project.wsgi.application'