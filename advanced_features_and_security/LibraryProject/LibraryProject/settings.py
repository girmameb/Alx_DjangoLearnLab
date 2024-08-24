# advanced_features_and_security/settings.py
# LibraryProject/settings.py

# Enable browser-side XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking attacks
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from sniffing MIME types
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Ensure your site is served over HTTPS
SECURE_SSL_REDIRECT = True

# HSTS (HTTP Strict Transport Security) settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

AUTH_USER_MODEL = 'bookshelf.CustomUser'
