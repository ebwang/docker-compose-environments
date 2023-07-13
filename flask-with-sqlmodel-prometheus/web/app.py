# app.py


from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        post = Actor(first_name, last_name)
        db.session.add(post)
        db.session.commit()
    posts = Actor.query.order_by(Actor.first_name.desc()).all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
