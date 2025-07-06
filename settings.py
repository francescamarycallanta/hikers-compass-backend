"""
settings.py — Main configuration file for the Django backend.

Why it's important?????
This file tells Django how the entire project should behave.
It sets up the database, installed apps, security, API support, CORS settings, and more.
Think of it as the central control panel of the backend.
"""

# Pathlib is used to define platform-independent file paths
from pathlib import Path

# BASE_DIR points to the root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
# ------------------------------------------------------------------------------

SECRET_KEY = 'your-secret-key-here'  # Load this from an environment variable in production

# DEBUG should be False in production for security
DEBUG = True

# This contains the domain names that are allowed to access the backend
ALLOWED_HOSTS = []  # E.g. ['yourapp.com', '127.0.0.1']


# ------------------------------------------------------------------------------
# Application definition — All the apps the project will use
# ------------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',         # Admin dashboard
    'django.contrib.auth',          # Authentication system
    'django.contrib.contenttypes',  # Content type framework
    'django.contrib.sessions',      # Session support (cookies)
    'django.contrib.messages',      # Messaging framework (flash messages)
    'django.contrib.staticfiles',   # Handles static files (CSS, JS)

    # Third-party apps
    'rest_framework',               # Enables Django REST API
    'corsheaders',                  # Allows cross-origin requests
    'rest_framework_simplejwt',     # Adds JWT authentication

    # Your app
    'hikerscompass',                # Main hiking backend app
]

# ------------------------------------------------------------------------------
# Middleware — Processes requests/responses before reaching views
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Enables CORS — allows frontend (on different domain) to talk to backend
    'django.middleware.security.SecurityMiddleware',  # Adds security headers
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages session cookies
    'django.middleware.common.CommonMiddleware',  # Handles general request tweaks
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection (for forms)
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authenticates users
    'django.contrib.messages.middleware.MessageMiddleware',  # Flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

# ------------------------------------------------------------------------------
# Root URL and WSGI config — entry points for serving the app
# ------------------------------------------------------------------------------

ROOT_URLCONF = 'appBackend.urls'  # Points to the project-level urls.py
WSGI_APPLICATION = 'appBackend.wsgi.application'  # Used for deployment (e.g., with Gunicorn)

# ------------------------------------------------------------------------------
# Database — defines where the data is stored
# ------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Lightweight, built-in database
        'NAME': BASE_DIR / 'db.sqlite3',         # Database file path
    }
}

# You can switch this to PostgreSQL like this:
# 'ENGINE': 'django.db.backends.postgresql',
# 'NAME': 'your_db',
# 'USER': 'your_user',
# 'PASSWORD': 'your_pass',
# 'HOST': 'localhost',
# 'PORT': '5432',

# ------------------------------------------------------------------------------
# Password Validation — ensures users choose strong passwords
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # e.g., min 8 characters
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Blocks passwords like "password123"
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Blocks all-number passwords
    },
]

# ------------------------------------------------------------------------------
# Internationalization — language, timezone, etc.
# ------------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True         # Enable translation support
USE_TZ = True           # Use timezone-aware datetimes

# ------------------------------------------------------------------------------
# Static Files — For CSS, JS, images (mostly for admin panel or future frontend)
# ------------------------------------------------------------------------------

STATIC_URL = 'static/'
# You could also add STATICFILES_DIRS or STATIC_ROOT for deployment


# ------------------------------------------------------------------------------
# Default Primary Key Field Type — Used for model IDs (auto-incrementing fields)
# ------------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ------------------------------------------------------------------------------
# Django REST Framework — Controls API behavior
# ------------------------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT tokens for login/auth
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # By default, require login for all views
    ),
}


# ------------------------------------------------------------------------------
# CORS Settings — Allow frontend (like React Native) to connect to backend
# ------------------------------------------------------------------------------

CORS_ALLOWED_ORIGINS = [
    "http://localhost:19006",  # React Native Expo dev server
    "http://127.0.0.1:8000",   # Backend running locally
    # Add production frontend here, e.g., "https://myhikingappisamazing.com"
]

# Optional: allow all (not recommended for production)
# CORS_ALLOW_ALL_ORIGINS = True

