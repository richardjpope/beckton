from beckton import app
from beckton import celery
from twilio.rest import TwilioRestClient

@celery.task
def send_sms(to_phone, message):
    client = TwilioRestClient(account=app.config['TWILLIO_SID'], token=app.config['TWILLIO_AUTH_TOKEN'])
    client.messages.create(to=to_phone, from_=app.config['TWILLIO_PHONE_NUMBER'], body=message)
