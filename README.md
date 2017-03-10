#Beckton - build groups of paying members

Note: still in development - it is a good idea to get in touch before using for real.

Beckton is a tool for creating a new group of paying members, using the [Conditional Commitment](https://kclpure.kcl.ac.uk/portal/en/publications/how-the-internet-can-overcome-the-collective-action-problem(7043d36c-a77f-4304-85ce-8987b4ba2903)/export.html
) design pattern -  payments are only taken if a target it met.

Beckton could be used for thigns like setting up a new union branch or a new cooperative purchasing group. It uses [GoCardless](https://gocardless.com) to create and manage payments and [Twillio](https://www.twilio.com/) to send updates.

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

##Settings
* ``` BECKTON_TARGET ``` The number of people who need to sign up before payments are taken
* ``` BECKTON_STATEMENT ``` The statement that people are agreeing to e.g. I will join a tea club if 10 other people do too
* ``` BECKTON_TERMS ``` An additional thing that people confirm e.g. I am a resident of Barking and Dagenham"
* ``` BECKTON_EXPLANATION ``` Some words explaining the context of this campaign. this is displaid on the 1st page. Markdown is OK.
* ``` BECKTON_RATES_LABEL ``` The label for the radio buttons for choosing which rate to pay e.g. what hours do you work?
* ``` BECKTON_RATES_CSV ``` What rate options and prices to display e.g. "4,Part-time (&pound;4 a month)|8,Full-time (&pound;8 a month)"
* ``` BECKTON_POSTCODE_AREAS_CSV ``` Limit signups to specific UK postcodes e.g. "SW9,EC1,BR4" Set to False to allow any postcode
* ``` BECKTON_SUCCESS ``` The message to display on the 1st page when the target has been met e.g. "The target has been met - someone will be in touch"
* ``` BECKTON_DIRECT_DEBIT_CURRENCY ``` The currency for direct debits (defaults to "GBP")
* ``` BECKTON_DIRECT_DEBIT_NAME ``` What the subscription should be called in GoCardless


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




https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2Fmemespring%2Fbeckton%2Ftree%2Fmaster