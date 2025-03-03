from flask import Flask
from application.database import db #Step 3 database


app = None

def create_app():
    app = Flask(__name__) #app.py as server code; this will work as server (the file name)
    app.debug = True # this will give error code and which is leading to the crashing of the application
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quizmaster.sqlite3"
    db.init_app(app=app) #Step 3- connect db with app
    app.app_context().push() # This will work in applciation context (flask) (else runtime error)
    return app

app = create_app()
from application.controllers import *
 #step 2
# from application.models import * #Step 4 optional if we added this in controlers.py


if __name__ == "__main__": # it will run only when we invoke this, might result in db problems if not present
    app.run()



