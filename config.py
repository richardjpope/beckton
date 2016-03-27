import os

class Config(object):
    DEBUG = False
    # MONGODB_DB = os.environ.get('MONGODB_DB', None)
    # MONGODB_HOST = os.environ.get('MONGODB_HOST', None)
    # SECRET_KEY = os.environ.get('SECRET_KEY', None)

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {'DB': "beckton_dev"}
    SECRET_KEY = 'not-a-secret'
    DATABASE_ENCRYPTION_KEY = "DO NOT USE THIS KEY XXXXXXXXXXXX" #do not use this in production
    CONDITION_TARGET = 10
    CONDITION_STATEMENT = "I will join a union if 400 other London Deliveroo drivers do the same"
    
    TWILLIO_SID = os.environ.get('TWILLIO_SID', None)
    TWILLIO_AUTH_TOKEN = os.environ.get('TWILLIO_AUTH_TOKEN', None)
    TWILLIO_PHONE_NUMBER = os.environ.get('TWILLIO_PHONE_NUMBER', None)

    CELERY_BROKER_URL='mongodb://localhost:27017/beckton-tasks'
    CELERY_RESULT_BACKEND='mongodb://localhost:27017/beckton-tasks'
    CELERY_TIMEZONE = 'Europe/London'

class TestingConfig(DevelopmentConfig):
    TESTING = True
    MONGODB_SETTINGS = {'DB': "beckton_test"}
    WTF_CSRF_ENABLED = False