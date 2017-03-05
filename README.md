#Beckton - build groups of paying members

Beckton is a tool for creating a new group of paying members, but only if enough people agree to join to make it worth while. It could be used include setting up a new union branch, or a new cooperative purchasing group. It uses [GoCardless](https://gocardless.com) to create and manage payments and [Twillio](https://www.twilio.com/) to send updates.

* [Screenshots](#screenshots)
* [Getting started](#getting-started)
* [Settings](#settings)
* [Testing](#testing)
* [Resetting the database](resetting-the-database)


##Screenshots
<img src="https://github.com/memespring/beckton/raw/master/docs/step1.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step2.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step3.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step4.png" width="250"/>
<img src="https://github.com/memespring/beckton/raw/master/docs/step5.png" width="250"/>

##Getting started

This section describes how to get a development copy of Beckton working.

You must have the following things installed before you start

* [Node](https://nodejs.org/en/)
* [Python](https://www.python.org)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)
* [MongoDB](https://www.mongodb.com)


Clone this repository and install the requirements:

```
git clone git+https://github.com/memespring/beckton.git
cd beckton
virtualenv .
source bin/activate
pip install -r requirements.txt
npm install
```

To run beckton, you need to run several different things:

To run the web app:

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

##Testing

Note: test coverage is currently much lower than it should be.

To run the tests:

```
source bin/activate
export SETTINGS='config.TestingConfig'
python tests.py
```

##Resetting the database
```
python manage.py reset
```

https://kclpure.kcl.ac.uk/portal/en/publications/how-the-internet-can-overcome-the-collective-action-problem(7043d36c-a77f-4304-85ce-8987b4ba2903)/export.html
