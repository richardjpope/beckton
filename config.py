import os
import json
from datetime import timedelta

class Config(object):
    DEBUG = os.environ.get('DEBUG', False)

    PREFERRED_URL_SCHEME = os.environ.get('PREFERRED_URL_SCHEME', 'https')

    MONGODB_HOST = os.environ.get('MONGO_URI', None)
    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    DATABASE_ENCRYPTION_KEY = os.environ.get('DATABASE_ENCRYPTION_KEY', None) # must be 16, 24 or 32 bytes long
    
    TWILLIO_SID = os.environ.get('TWILLIO_SID', None)
    TWILLIO_AUTH_TOKEN = os.environ.get('TWILLIO_AUTH_TOKEN', None)
    TWILLIO_PHONE_NUMBER = os.environ.get('TWILLIO_PHONE_NUMBER', None)

    GOCARDLESS_ACCESS_TOKEN = os.environ.get('GOCARDLESS_ACCESS_TOKEN', None)
    GOCARDLESS_ENVIRONMENT = os.environ.get('GOCARDLESS_ENVIRONMENT', 'sandbox')

    BECKTON_TARGET = int(os.environ.get('BECKTON_TARGET', 0))
    BECKTON_STATEMENT = os.environ.get('BECKTON_STATEMENT', None)
    BECKTON_TERMS = os.environ.get('BECKTON_TERMS', None)
    BECKTON_EXPLANATION = os.environ.get('BECKTON_EXPLANATION', None) #markdown OK here
    BECKTON_RATES_LABEL = os.environ.get('BECKTON_RATES_LABEL', '')
    BECKTON_RATES_CSV = os.environ.get('BECKTON_RATES_CSV', '')
    BECKTON_POSTCODE_AREAS_CSV = os.environ.get('BECKTON_POSTCODE_AREAS_CSV', False) # set to False to allow any postcode
    BECKTON_SUCCESS = os.environ.get('BECKTON_SUCCESS', '')
    BECKTON_DIRECT_DEBIT_CURRENCY = os.environ.get('BECKTON_DIRECT_DEBIT_CURRENCY', 'GBP')
    BECKTON_DIRECT_DEBIT_NAME = os.environ.get('BECKTON_DIRECT_DEBIT_NAME', '')
    
    CELERY_TIMEZONE = 'UTC'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 20
    CELERY_BROKER_URL = os.environ.get('REDIS_URL', None)
    CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', None)
    # CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE', None)
    CELERYBEAT_SCHEDULE = {
    'send_halfway_message': {
        'task': 'beckton.tasks.send_halfway_message',
        'schedule': timedelta(seconds=30)
    },
    'send_target_complete_message': {
        'task': 'beckton.tasks.send_target_complete_message',
        'schedule': timedelta(seconds=30)
    },
    'create_subscriptions': {
        'task': 'beckton.tasks.create_subscriptions',
        'schedule': timedelta(seconds=30)
    },
}

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_DB = "beckton_dev"
    SECRET_KEY = 'not-a-secret'
    DATABASE_ENCRYPTION_KEY = "DO NOT USE THIS KEY XXXXXXXXXXXX" #do not use this in production

    TWILLIO_SID = os.environ.get('TWILLIO_SID', None)
    TWILLIO_AUTH_TOKEN = os.environ.get('TWILLIO_AUTH_TOKEN', None)
    TWILLIO_PHONE_NUMBER = os.environ.get('TWILLIO_PHONE_NUMBER', None)

    CELERY_BROKER_URL='mongodb://localhost:27017/beckton-tasks'
    CELERY_RESULT_BACKEND='mongodb://localhost:27017/beckton-tasks'

    BECKTON_DIRECT_DEBIT_NAME = 'Beckton'
    BECKTON_TARGET = 2
    BECKTON_STATEMENT = "I will join the union if 10 other widget makers will do the same"
    BECKTON_TERMS = "I work for Widget Makers LLP (Delaware)"
    BECKTON_EXPLANATION = "Employees of [Widget Makers](#) are not currently paid the living wage. If we can get enough people to join the union, we can campaign for change." #markdown OK here
    BECKTON_SUCCESS = "The target has been met, someone will be in touch"
    BECKTON_RATES_LABEL = "What hours do you work?"
    BECKTON_RATES_CSV = "4,Part-time (&pound;4 a month)|8,Full-time (&pound;8 a month)"
    BECKTON_POSTCODE_AREAS_CSV = "SW9,EC1,BR4" # set to False to allow any postcode

class TestingConfig(DevelopmentConfig):
    TESTING = True
    MONGODB_SETTINGS = {'DB': "beckton_test"}
    WTF_CSRF_ENABLED = False