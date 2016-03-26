from flask import Flask, request, redirect, render_template, url_for
from flask.ext.mongoengine import MongoEngine
import jinja2
import os
import forms
import models

app = Flask(__name__)
app.config.from_object(os.environ.get('SETTINGS', 'config.DevelopmentConfig'))
db = MongoEngine(app)

@app.route("/", methods=['GET', 'POST'])
def condition():

    condition_statement = app.config['CONDITION_STATEMENT']
    form = forms.Commitment()

    if request.method == 'POST' and form.validate():
        commitment = models.Commitment(app.config['DATABASE_ENCRYPTION_KEY'])
        commitment.name = form.data['name']
        commitment.mobile_number = form.data['mobile_number']
        commitment.save()

        return redirect(url_for('committed'))

    return render_template('condition.html', condition_statement=condition_statement, form=form)

@app.route("/done")
def committed():
    commitment_count = models.Commitment.objects.count()
    return render_template('committed.html', commitment_count=commitment_count)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
