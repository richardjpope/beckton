from flask import Flask, request, redirect, render_template
import jinja2
import os

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
