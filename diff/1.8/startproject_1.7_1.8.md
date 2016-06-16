
```diff
--- release/1.7/startproject_settings.py	2016-06-16 01:06:49.304211530 -0300
+++ release/1.8/startproject_settings.py	2016-06-16 01:06:55.512211529 -0300
@@ -3 +2,0 @@
-ADMIN_FOR = ()
@@ -14 +12,0 @@
-COMMENTS_ALLOW_PROFANITIES = False
@@ -43,0 +42,2 @@
+EMAIL_SSL_CERTFILE = None
+EMAIL_SSL_KEYFILE = None
@@ -44,0 +45 @@
+EMAIL_TIMEOUT = None
@@ -77 +78 @@
-MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware')
+MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware', 'django.middleware.security.SecurityMiddleware')
@@ -84 +84,0 @@
-PROFANITIES_LIST = ()
@@ -86,0 +87,4 @@
+SECURE_BROWSER_XSS_FILTER = False
+SECURE_CONTENT_TYPE_NOSNIFF = False
+SECURE_HSTS_INCLUDE_SUBDOMAINS = False
+SECURE_HSTS_SECONDS = 0
@@ -88 +92,3 @@
-SEND_BROKEN_LINK_EMAILS = False
+SECURE_REDIRECT_EXEMPT = []
+SECURE_SSL_HOST = None
+SECURE_SSL_REDIRECT = False
@@ -112,2 +118,3 @@
-TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth', 'django.core.context_processors.debug', 'django.core.context_processors.i18n', 'django.core.context_processors.media', 'django.core.context_processors.static', 'django.core.context_processors.tz', 'django.contrib.messages.context_processors.messages')
-TEMPLATE_DEBUG = True
+TEMPLATES = [{'DIRS': [], 'APP_DIRS': True, 'OPTIONS': {'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages']}, 'BACKEND': 'django.template.backends.django.DjangoTemplates'}]
+TEMPLATE_CONTEXT_PROCESSORS = ('django.contrib.auth.context_processors.auth', 'django.template.context_processors.debug', 'django.template.context_processors.i18n', 'django.template.context_processors.media', 'django.template.context_processors.static', 'django.template.context_processors.tz', 'django.contrib.messages.context_processors.messages')
+TEMPLATE_DEBUG = False
@@ -123 +129,0 @@
-TRANSACTIONS_MANAGED = False
```
