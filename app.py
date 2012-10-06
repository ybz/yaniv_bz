import os

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.jinja_env.filters['static'] = lambda name: url_for('static', filename=name)

@app.route('/')
def hello():
    return render_template('index.tmpl')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



