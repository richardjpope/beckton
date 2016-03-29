from beckton import app
from beckton import celery
from twilio.rest import TwilioRestClient

@celery.task
def send_committed_message(commitment):
    message = "You have committed to the following: \"%s\". You are number %d We'll keep you updated." % app.config['CONDITION_STATEMENT']
    client = TwilioRestClient(account=app.config['TWILLIO_SID'], token=app.config['TWILLIO_AUTH_TOKEN'])
    client.messages.create(to=commitment.mobile_number, from_=app.config['TWILLIO_PHONE_NUMBER'], body=message)

