# settings.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set DEBUG based on environment variable
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Retrieve ALLOWED_HOSTS from environment variables
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

# Configure Django to trust the X-Forwarded-Proto header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Enforce HTTPS by redirecting all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = True

# Enable HTTP Strict Transport Security (HSTS) for one year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000

# Include all subdomains in the HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow preloading of the HSTS policy
SECURE_HSTS_PRELOAD = True

# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Prevent your site from being framed to protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser’s XSS filtering to help prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True


AUTH_USER_MODEL = 'bookshelf.CustomUser'
