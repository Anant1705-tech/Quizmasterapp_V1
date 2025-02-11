#application.database -> Tjem models will think there is one more folder in the folder it is existing and inside that folder w

from .database import db    #. will make it not to search in the root folder look in the application folder thats it 

# we have two model user, admin

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username =  db.Column(db.String(), unique = True, nullable = False)
    email = db.Column(db.String(), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    type = db.Column(db.String(), default = "general")
    details = db.relationship("Info", backref = "creator")

class Info(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    atr_name = db.Column(db.String(), nullable = False)
    atr_value  = db.Column(db.String(), nullable = False)
    c_name = db.Column(db.String(), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey ("user.id"), nullable = False)


