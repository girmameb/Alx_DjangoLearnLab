# django_blog/settings.py

import os
from pathlib import Path

# django_blog/settings.py

ROOT_URLCONF = 'django_blog.urls'  # Adjust this to match your project's URL configuration

# django_blog/settings.py

DEBUG = True  # Ensure this is set according to your needs

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add allowed hosts

BASE_DIR = Path(__file__).resolve().parent.parent

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog/templates')],  # Add this line
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

# settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'blog', 'static')]

# In your settings.py
LOGIN_REDIRECT_URL = '/profile/'  # or 'profile' if using named URLs


# django_blog/settings.py

INSTALLED_APPS = [
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # Ensure this line is present
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'blog',  # Your blog app
    'taggit',  # Add this line for django-taggit
    # Add other apps here if necessary
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Ensure this line is here
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # This should come after SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# django_blog/settings.py
import secrets
print(secrets.token_urlsafe(50))

SECRET_KEY = '12345678'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",  # Adjust this if needed
    }
}
