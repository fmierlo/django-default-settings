ABSOLUTE_URL_OVERRIDES = {}
ADMINS = ()
ADMIN_FOR = ()
ADMIN_MEDIA_PREFIX = '/media/'
ALLOWED_INCLUDE_ROOTS = ()
APPEND_SLASH = True
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
BANNED_IPS = ()
CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
COMMENTS_ALLOW_PROFANITIES = False
COMMENTS_BANNED_USERS_GROUP = None
COMMENTS_FIRST_FEW = 0
COMMENTS_MODERATORS_GROUP = None
COMMENTS_SKETCHY_USERS_GROUP = None
DATABASE_ENGINE = ''
DATABASE_HOST = ''
DATABASE_NAME = ''
DATABASE_OPTIONS = {}
DATABASE_PASSWORD = ''
DATABASE_PORT = ''
DATABASE_USER = ''
DATETIME_FORMAT = 'N j, Y, P'
DATE_FORMAT = 'N j, Y'
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False
DEFAULT_CHARSET = 'utf-8'
DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
DEFAULT_INDEX_TABLESPACE = ''
DEFAULT_TABLESPACE = ''
DISALLOWED_USER_AGENTS = ()
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[Django] '
EMAIL_USE_TLS = False
FILE_CHARSET = 'utf-8'
FILE_UPLOAD_HANDLERS = ('django.core.files.uploadhandler.MemoryFileUploadHandler', 'django.core.files.uploadhandler.TemporaryFileUploadHandler')
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_TEMP_DIR = None
FIXTURE_DIRS = ()
FORCE_SCRIPT_NAME = None
IGNORABLE_404_ENDS = ('mail.pl', 'mailform.pl', 'mail.cgi', 'mailform.cgi', 'favicon.ico', '.php')
IGNORABLE_404_STARTS = ('/cgi-bin/', '/_vti_bin', '/_vti_inf')
INSTALLED_APPS = []
INTERNAL_IPS = ()
LANGUAGES = (('ar', 'Arabic'), ('bg', 'Bulgarian'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('es', 'Spanish'), ('es-ar', 'Argentinean Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy-nl', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('zh-cn', 'Simplified Chinese'), ('zh-tw', 'Traditional Chinese'))
LANGUAGES_BIDI = ('he', 'ar', 'fa')
LANGUAGE_CODE = 'en-us'
LANGUAGE_COOKIE_NAME = 'django_language'
LOCALE_PATHS = ()
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
MANAGERS = ()
MEDIA_ROOT = ''
MEDIA_URL = ''
MIDDLEWARE_CLASSES = ('django.middleware.common.CommonMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware')
MONTH_DAY_FORMAT = 'F j'
PASSWORD_RESET_TIMEOUT_DAYS = 3
PREPEND_WWW = False
PROFANITIES_LIST = ('asshat', 'asshead', 'asshole', 'cunt', 'fuck', 'gook', 'nigger', 'shit')
SECRET_KEY = '01234567890123456789012345678901234567890123456789'
SEND_BROKEN_LINK_EMAILS = False
SERVER_EMAIL = 'root@localhost'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_SECURE = False
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_FILE_PATH = None
SESSION_SAVE_EVERY_REQUEST = False
SETTINGS_MODULE = 'project.defaults'  ###
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.auth', 'django.core.context_processors.debug', 'django.core.context_processors.i18n', 'django.core.context_processors.media')
TEMPLATE_DEBUG = False
TEMPLATE_DIRS = ()
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.load_template_source', 'django.template.loaders.app_directories.load_template_source')
TEMPLATE_STRING_IF_INVALID = ''
TEST_DATABASE_CHARSET = None
TEST_DATABASE_COLLATION = None
TEST_DATABASE_NAME = None
TEST_RUNNER = 'django.test.simple.run_tests'
TIME_FORMAT = 'P'
TIME_ZONE = 'America/Chicago'
TRANSACTIONS_MANAGED = False
URL_VALIDATOR_USER_AGENT = 'Django/1.1.3 (http://www.djangoproject.com)'
USE_ETAGS = False
USE_I18N = True
YEAR_MONTH_FORMAT = 'F Y'
