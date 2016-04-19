import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '12345'
DEBUG = False
ROOT_URLCONF = 'urls'

ALLOWED_HOSTS = [
    '127.0.0.1',
]

MIDDLEWARE_CLASSES = [
    'middleware.GzipRequestBodyMiddleware',
]
