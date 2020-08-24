import os

from signals.settings.base import *  # noqa

SECRET_KEY = 'insecure'
DEBUG = True
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SIGNALS_AUTHZ = {
    'JWKS_URL': "http://dex:5556/keys",
    'ALWAYS_OK': False,
    'USER_ID_FIELD': 'email'
}

SITE_DOMAIN = 'localhost:8000'

INSTALLED_APPS += [  # noqa
    'debug_toolbar',
]
MIDDLEWARE.append(  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEST_LOGIN = os.getenv('TEST_LOGIN', 'signals.admin@example.com')

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.Optimistic'

# ML_TOOL_ENDPOINT = 'https://acc.api.data.amsterdam.nl/signals_mltool'

try:
    from signals.settings.local import *  # noqa
except ImportError:
    pass


# from django.core import mail
# def send_email():
#     subject = "Testing"
#     message = "Test email functionality"
#     from_email = 'abhisheksirohi19@gmail.com'
#     recipient_list = ['mshoaib9942@gmail.com']
#     return mail.send_mail(subject=subject, message=message, from_email=from_email,
#                             recipient_list=recipient_list)

# connection = mail.get_connection()
# connection.open()
# send_email()
# connection.close()



def show_toolbar(request):
    return False  # True to enable Django Debug Toolbar (very slow)


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# Set console logging to DEBUG
LOGGING['handlers'].update({  # noqa F405
    'console': {
        'level': 'WARNING',
        'class': 'logging.StreamHandler',
        'formatter': 'console',
    },
})

# Log queries to the console
LOGGING['loggers'].update({  # noqa F405
    'django.db.backends': {
        'level': 'WARNING',
        'handlers': ['console', ],
    }
})
