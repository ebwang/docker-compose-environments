# models.py


import datetime
from app import db


#class Post(db.Model):
#
#    __tablename__ = 'posts'
#
#    id = db.Column(db.Integer, primary_key=True)
#    text = db.Column(db.String, nullable=False)
#    date_posted = db.Column(db.DateTime, nullable=False)
#
#    def __init__(self, text):
#        self.text = text
#        self.date_posted = datetime.datetime.now()


class Actor(db.Model):
    
    __tablename__ = 'actor'

    actor_id = db.Column(db.Integer,  primary_key=True )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = datetime.datetime.now()
