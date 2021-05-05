"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'example_app',
)

ROOT_URLCONF = 'example_app.urls'

SECRET_KEY = 'redundant'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
