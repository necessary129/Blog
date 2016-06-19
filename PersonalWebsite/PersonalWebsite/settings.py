"""
Django settings for PersonalWebsite project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9v-=6qb&t95(b%x5sf5q##!rgv*t67=f)23b4a1lmidnl%q(hx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PersonalWebsite.urls'

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

WSGI_APPLICATION = 'PersonalWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

NAME = "Shamil K Muhammed"

SUBHEADING = "My space where i write about everything."

TWITTER_URL = "https://twitter.com/noteasham/"

GITHUB_URL = "https://github.com/necessary129/"

EMAIL_FROM = "{name} <noreply@yourdomain.com>"

EMAIL_TO = ["mail@yourdomain.org"]

SMTP_HOST = "localhost"

SMTP_PORT = 25

SMTP_STARTTLS = True

SMTP_AUTH_USERNAME = None

SMTP_AUTH_PASSWORD = None

EMAIL_HTML = """\
<!DOCTYPE html>
<html>
<head></head>
<body>
Hi,<br/>
<p>You have recieved a new message from <strong>{name} (<a href="mailto:{email}">{email}</a>)</strong></p>
<p>Message:</p>
<pre>
{message}
</pre>
</body>
</html>
"""

EMAIL_TEXT = """\
Hi you have recieved a new message from {name} ({email}).

Message:

{message}
"""

RECAPTCHA_SECRET = "secret"
RECAPTCHA_SITE_KEY = "key"

ABOUT = """\
Hello,

My name is Shamil K Muhammed. I am from a small town
called [Kalikavu][1] and I am studying at class 9th
in [Crescent High School, Adakkakundu][2]. I am an experienced coder
and a N00B writer.

I try to add content here. Wish me good luck!

[1]: https://en.wikipedia.org/wiki/Kalikavu
[2]: https://www.facebook.com/chssadakkakundukalikavu

"""

ABOUT_SUBTITLE = "This is what I am."

GA_ID = "UA-78258666-1"

DISQUS_SHORTNAME = "sham-blog"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

try:
    from local_settings import *
except ImportError:
    print("You have not set up the local settings. Please set it up.")
    exit(1)

import markdown
ABOUT = markdown.markdown(ABOUT)