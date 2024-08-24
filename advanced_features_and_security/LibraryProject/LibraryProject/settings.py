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


AUTH_USER_MODEL = 'bookshelf.CustomUser'
