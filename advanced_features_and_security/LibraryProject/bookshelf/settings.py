# advanced_features_and_security/settings.py
# settings.py

# Set DEBUG to False in product
import os

# Get DEBUG setting from environment

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set DEBUG based on environment variable
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Retrieve ALLOWED_HOSTS from environment variables
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

AUTH_USER_MODEL = 'bookshelf.CustomUser'
