from flask import request, redirect, render_template, url_for
from mongoengine import NotUniqueError
from beckton import app
import forms
import models
import tasks

@app.route("/test/pay")
def pay_start():
    import gocardless
    gocardless.set_details(app_id="DUMMY_APP",
        app_secret="INSERT_APP_SECRET_HERE",
        access_token="INSERT_MERCHANT_ACCESS_TOKEN",
        merchant_id="INSERT_MERCHANT_ID")
    gocardless.client.merchant()
    return "hello"

@app.route("/test")
def test():
    tasks.send_sms.delay('+447976730458', 'TESTING TESTING')
    return "done"

@app.route("/", methods=['GET', 'POST'])
def condition():

    condition_statement = app.config['CONDITION_STATEMENT']
    form = forms.Commitment()
    duplicate = False

    if request.method == 'POST' and form.validate():
        commitment = models.Commitment(app.config['DATABASE_ENCRYPTION_KEY'])
        commitment.name = form.data['name']
        commitment.mobile_number = form.data['mobile_number']
        try:
            commitment.save()
            return redirect(url_for('committed'))
        except NotUniqueError:
            duplicate = True

    return render_template('condition.html', condition_statement=condition_statement, form=form, duplicate=duplicate)

@app.route("/done")
def committed():
    commitment_count = models.Commitment.objects.count()
    return render_template('committed.html', commitment_count=commitment_count)
