#application.database -> Tjem models will think there is one more folder in the folder it is existing and inside that folder w

from .database import db    #. will make it not to search in the root folder look in the application folder thats it 

# we have two- user, admin

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username =  db.Column(db.String(), unique = True, nullable = False)
    email = db.Column(db.String(), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    type = db.Column(db.String(), default = "general")
    
    # details = db.relationship("Info", backref = "creator")

class Subject(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    subject_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    chapter_name = db.Column(db.String(), nullable=False)
    number_of_questions = db.Column(db.Integer(), nullable=False)

class Quizzes(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    date_of_quiz = db.Column(db.Date())
    time_duration = db.Column(db.String())
    question_statement = db.Column(db.String(), nullable=False)
    option1 = db.Column(db.String(), nullable=False)
    option2 = db.Column(db.String(), nullable=False)
    option3 = db.Column(db.String(), nullable=False)
    option4 = db.Column(db.String(), nullable=False)
    correct_answer = db.Column(db.String(), nullable=False)


    


