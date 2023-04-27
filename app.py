import flask
from flask import render_template, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/<value>/', methods=['GET',])
def index(value=''):
    return render_template('my_template.html', value=value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')