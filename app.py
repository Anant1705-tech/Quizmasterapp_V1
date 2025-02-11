from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/login')


def login_page():
    return render_template('Login Page.html')

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask 

# from application.database import db

# app = None

# def create_app():
#     app = Flask(__name__)
#     app.debug = True 
    
#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quizmaster.sqlite3"
#     db.init_app(app) #3  #connect database 
    
#     app.app_context().push()
#     return app 

# app = create_app()
# from application.controllers import *  #2 controllers
#  # from application.models import * # indirect connection using controllers

# if __name__ == '__main__':
#     app.run(debug=True)