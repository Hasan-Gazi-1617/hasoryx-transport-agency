import os
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev-only-change-this-secret-key')
DEBUG=os.environ.get('DJANGO_DEBUG','True').lower()=='true'
ALLOWED_HOSTS=[x.strip() for x in os.environ.get('DJANGO_ALLOWED_HOSTS','127.0.0.1,localhost,.onrender.com').split(',') if x.strip()]
INSTALLED_APPS=['django.contrib.staticfiles','core']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='config.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request']}}]
WSGI_APPLICATION='config.wsgi.application'
# Dummy backend satisfies Django's connection handler without creating or using a database.
DATABASES={'default':{'ENGINE':'django.db.backends.dummy'}}
LANGUAGE_CODE='en-us'; TIME_ZONE='Asia/Dhaka'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; STATICFILES_DIRS=[BASE_DIR/'static']; STATIC_ROOT=BASE_DIR/'staticfiles'
STORAGES={'default':{'BACKEND':'django.core.files.storage.FileSystemStorage'},'staticfiles':{'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}}
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
SECURE_CONTENT_TYPE_NOSNIFF=True; X_FRAME_OPTIONS='DENY'
