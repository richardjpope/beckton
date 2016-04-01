NEXT: use celery beat to send messages at 50% and 100%
* task: a bit of visual design
* As a worker, I want to be alerted when certain milestones are reached
* As a worker I would like payments to be taken if the target is met
* As a customer, I want to be able to pledge my support (somehow)
* Task: js/css assets should be locally hosted
  - foundation [tick]
  - jquery
* As a coordinator I want to be able to message people in exceptional circumstances (e.g. turn up to a PR event)
* Task: add tests and exception handing for sending sms / tasks.py
* Task: add modernizer
* Task: postcode areas error message in forms.py should replace last comma with 'or'.
* Task: add a licence
* Task: add scss setup to readme

.alert-box {
  text-align:center;
}

DONE:

* As a coordinator I want to be able to limit a campaign to particular postcode districts
* As a worker I want to record if I work part-time or full-time so I can be charged the correct rate
* As a worker I want to be able to join the union and setup a direct debit
* As a worker who has signed up, I get an sms confirming
* As a worker I want to be able to sign up (name, contact details, address)
  - pledge
  - disallow duplicate phone numbers
  - make sure that form fields don't remember previous input
  - disallow duplicate phone numbers <- need to check on first page AND on final save

* As a worker or customer, I want to see numbers signed up
  - show on confirmation page up page 
  - show progress bar on start page

* As a worker, I  want to be reassured that my data will be safe
* As a worker/customer/other I want to understand the background of the campaign
* Task: Make all alerts happen via a que