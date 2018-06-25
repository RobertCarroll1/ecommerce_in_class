from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*=stu(-84csgpzfcybcmq(us8g@lhxt=cq$k8s*kv*)%i_2x#8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
