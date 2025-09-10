from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'dev-secret'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework',
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
ROOT_URLCONF = 'csi_erp.urls'
TEMPLATES=[{ 'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':[
 'django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']} }]
WSGI_APPLICATION = 'csi_erp.wsgi.application'
DATABASES = { 'default': {'ENGINE':'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'} }
LANGUAGE_CODE='pt-br'; TIME_ZONE='America/Recife'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
ALLOWED_HOSTS = ['erp-osc-monorepo.onrender.com']

CSRF_TRUSTED_ORIGINS = ['https://erp-osc-monorepo.onrender.com']

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# === Render/Docker: DB & Static files ===
import os
import dj_database_url

# DEBUG via variável de ambiente (default: False em produção)
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Banco de dados: usa DATABASE_URL (Render) e cai para SQLite em dev
DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        ssl_require=True,
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
    )
}

# Arquivos estáticos (WhiteNoise)
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Respeitar HTTPS atrás do proxy do Render
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
