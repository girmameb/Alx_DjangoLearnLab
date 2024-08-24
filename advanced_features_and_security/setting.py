# settings.py
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_features_and_security.settings')

AUTH_USER_MODEL = 'bookshelf.CustomUser'
