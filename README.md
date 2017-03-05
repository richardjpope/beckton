Beckton is a tool for creating a new group of paying members, but only if enough people agree to join to make it worth while.

Examples of how it could be used include setting up a new union branch, or a new coopertive buying group.

It uses GoCardless to create and manage payments and Twillio to send updates.

##Screenshots
<img src="https://github.com/memespring/beckton/raw/master/docs/step1.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step2.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step3.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step4.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step5.png" width="250"/>

##Installing a local development copy

Must have installed:

Node
Python + virtualenv
MongoDB


Clone this repository and then:

```
virtualenv .
source bin/activate
pip install -re requirements.txt
npm install
```


##Running a local copy

Run the web app:

```
source bin/activate
export SETTINGS='config.DevelopmentConfig'
export GOCARDLESS_ACCESS_TOKEN='ENTER YOUR GO CARDLESS ACCESS TOKEN'
python server.py
```

Run the scheduler (in a separate terminal):
```
source bin/activate
export SETTINGS='config.DevelopmentConfig'
celery -A beckton.celery beat
```

Run the message que (in a separate terminal):
```
source bin/activate
export SETTINGS='config.DevelopmentConfig'
export GOCARDLESS_ACCESS_TOKEN='ENTER YOUR GO CARDLESS ACCESS TOKEN'
export TWILLIO_SID='ENTER YOUR TWILLIO SID'
export TWILLIO_AUTH_TOKEN='ENTER YOUR TWILLIO AUTH TOKEN'
export TWILLIO_PHONE_NUMBER='ENTER YOUR TWILIO PHONE NUMBER'
celery -A beckton.celery worker
```

Run the assets compiler (in a separate terminal):

```
grunt
```

##Running tests locally

```
source bin/activate
export SETTINGS='config.TestingConfig'
python tests.py
```

##Management commands

###Reset everything
```
python manage.py reset
```

## Notes:
https://kclpure.kcl.ac.uk/portal/en/publications/how-the-internet-can-overcome-the-collective-action-problem(7043d36c-a77f-4304-85ce-8987b4ba2903)/export.html
