# advanced_features_and_security/settings.py
# settings.py

# Set DEBUG to False in product
import os

# Get DEBUG setting from environment

import os

import MIDDLEWARE
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set DEBUG based on environment variable
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Retrieve ALLOWED_HOSTS from environment variables
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

# settings.py

INSTALLED_APPS += ['csp']
MIDDLEWARE += ['csp.middleware.CSPMiddleware']

# Define CSP settings
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'", 'https://cdnjs.cloudflare.com')
CSP_IMG_SRC = ("'self'", 'data:')
CSP_FONT_SRC = ("'self'", 'https://fonts.gstatic.com')


AUTH_USER_MODEL = 'bookshelf.CustomUser'
