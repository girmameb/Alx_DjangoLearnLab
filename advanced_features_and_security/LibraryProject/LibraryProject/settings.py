# advanced_features_and_security/settings.py
# LibraryProject/settings.py
# settings.py
import MIDDLEWARE

# Set DEBUG to False in production
DEBUG = False

# Security settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Ensure HTTPS is used
SECURE_SSL_REDIRECT = True

# settings.py

INSTALLED_APPS += ['csp']
MIDDLEWARE += ['csp.middleware.CSPMiddleware']

# Define CSP settings
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'", 'https://cdnjs.cloudflare.com')
CSP_IMG_SRC = ("'self'", 'data:')
CSP_FONT_SRC = ("'self'", 'https://fonts.gstatic.com')

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
