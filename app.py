import os
import json

from flask import Flask, render_template, url_for, make_response
import lorem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.debug = True
app.jinja_env.filters['static'] = lambda name: url_for('static', filename=name)

@app.route('/')
def hello():
    return render_template('index.tmpl')

@app.route('/test_api')
def test_api():
    ret_obj = [lorem.make_message(i) for i in range(50)]
    ret_json = json.dumps(ret_obj)
    res = make_response(ret_json)
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


