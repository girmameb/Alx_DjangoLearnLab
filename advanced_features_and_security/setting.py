# advanced_features_and_security/settings.py

# Add 'accounts' app to INSTALLED_APPS
INSTALLED_APPS = [
    # other apps
    'accounts',
    # ...
]

# Set the custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'
