from beckton import app
from beckton import celery
from twilio.rest import TwilioRestClient
import gocardless_pro
import models
import time

def _send_sms(mobile_number, message):
    print "sending message"
    client = TwilioRestClient(account=app.config['TWILLIO_SID'], token=app.config['TWILLIO_AUTH_TOKEN'])
    client.messages.create(to=mobile_number, from_=app.config['TWILLIO_PHONE_NUMBER'], body=message)

@celery.task
def send_committed_message(mobile_number):
    message = "You have committed to the following: \"%s\". We'll keep you updated." % app.config['BECKTON_STATEMENT']
    _send_sms(mobile_number, message)

@celery.task
def send_halfway_message():
  if len(models.Milestone.objects(name='halfway-message-sent')) == 0:
      commitment_count = models.Commitment.objects.count()
      if float(commitment_count) >= (float(app.config['BECKTON_TARGET']) / 2):
          milestone = models.Milestone(name='halfway-message-sent')
          if milestone.save():

              message = "%d other people have committed to the following: \"%s\"! We'll let you know if the target is met." % (commitment_count, app.config['BECKTON_STATEMENT'])

              for commitment in models.Commitment.objects():
                  _send_sms(commitment.mobile_number, message)
                  time.sleep(1)

@celery.task
def send_target_complete_message():
  if len(models.Milestone.objects(name='target-met-message-sent')) == 0:
      commitment_count = models.Commitment.objects.count()
      if float(commitment_count) >= (float(app.config['BECKTON_TARGET'])):
          milestone = models.Milestone(name='target-met-message-sent')
          if milestone.save():
              
              message = "%d other people have committed to the following: \"%s\". This means the target has been met!" % (commitment_count, app.config['BECKTON_STATEMENT'])

              for commitment in models.Commitment.objects():
                  _send_sms(commitment.mobile_number, message).delay()
                  time.sleep(1)

@celery.task
def create_subscriptions():
  if len(models.Milestone.objects(name='subscriptions-created')) == 0:
      commitment_count = models.Commitment.objects.count()
      if float(commitment_count) >= (float(app.config['BECKTON_TARGET'])):
          milestone = models.Milestone(name='subscriptions-created')
          if milestone.save():

              for commitment in models.Commitment.objects():
                  
                  client = gocardless_pro.Client(access_token=app.config['GOCARDLESS_ACCESS_TOKEN'], environment=app.config['GOCARDLESS_ENVIRONMENT'])
                  
                  client.subscriptions.create(params={
                    "amount": str(commitment.rate),
                    "currency": app.config['BECKTON_DIRECT_DEBIT_CURRENCY'],
                    "name": app.config['BECKTON_DIRECT_DEBIT_NAME'],
                    "interval_unit": "monthly",
                    "day_of_month":  "1",
                    "links": {
                      "mandate": commitment.gocardless_mandate_id
                    }
                  })

                  time.sleep(1)
