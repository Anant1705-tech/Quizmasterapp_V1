from flask import Flask, render_template,redirect,request, url_for 
from flask import current_app as app #curret app refers to app.py 
from .models import * 


@app.route("/")
def start_page():
    return redirect(url_for("login"))



@app.route("/login",methods=["GET","POST"]) #url with specific http method gives specific results
def login():
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username=username).first() #LHS is column name RHS is the data fetched from the form in live server
        if this_user:
            if this_user.password == pwd:
                if this_user.type == "admin":
                    return redirect(url_for("admin_dashboard"))
                    # return render_template("Admin Dashboard.html",this_user=this_user) #LHS is jinja also linked in the admin dash and RHS is the data feched
                else:
                    return render_template("User Dashboard.html", this_user=this_user)
            else:
                return "Incorrect Password"
       
        else:
            return "User does not exists"
   
    return render_template("Login Page.html")




@app.route("/register",methods=["GET","POST"]) #url with specific http method gives specific results
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        pwd = request.form.get("pwd") #pwd is the temporory variable in which we stored the value from backend var to update in the db
        this_user = User.query.filter_by(username=username).first()
        if this_user:
            return "user already exists"
        else:
            new_user = User(username = username, email = email, password=pwd) #LHS is column name RHS is the data fetched from the form in live server.
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
    return render_template("Register.html")



@app.route("/admin/dashboard")
def admin_dashboard():
    subjects = Subject.query.all()
    return render_template("Admin Dashboard.html", subjects = subjects, )



@app.route("/admin/new-subject", methods = ["GET","POST"])
def new_subject():
    if request.method == "POST":
        subject_name = request.form.get("subject_name")
        description =  request.form.get("description")
        new_subject = Subject(subject_name = subject_name, description = description)
        db.session.add(new_subject)
        db.session.commit()

        return("Added the subject successfully")
        # return redirect("/admin/dashboard")
    return render_template("New Subject.html")


@app.route("/new-chapter/<int:subject_id>", methods = ["GET", "POST"])
def new_chapter(subject_id):
    subject = Subject.query.get(subject_id) #subject table and id column in subject_id
    if not subject:
        return("Added the chapter successfully")
        # return redirect("/admin/dashboard")
    if request.method == "POST":
        chapter_name = request.form.get("chapter_name")
        description = request.form.get("description")
        new_chapter = Chapter(chapter_name = chapter_name, description = description, subject_id = subject_id)
        db.session.add(new_chapter)
        db.session.commit()
        return redirect("/admin/dashboard")

    return render_template("New Chapter.html", subject = subject, subject_id = subject.id)


@app.route("/delete/chapter/<int:chapter_id>", methods=["POST"])
def delete_chapter(chapter_id):
    chapter = Chapter.query.get(chapter_id)
    if chapter:
        db.session.delete(chapter)
        db.session.commit()
    return redirect(url_for("admin_dashboard"))




@app.route("/admin/new-quiz/<int:chapter_id>", methods=["GET", "POST"])
def new_quiz(chapter_id):
    chapter = Chapter.query.get(chapter_id)  # Fetch the chapter by ID
    if not chapter:
        flash("Chapter not found!", "danger")
        return redirect("/admin/dashboard")

    if request.method == "POST":
        quiz_title = request.form.get("quiz_title")
        date_of_quiz = request.form.get("date_of_quiz")
        time_duration = request.form.get("time_duration")
        remarks = request.form.get("remarks")

        new_quiz = Quiz(
            quiz_title=quiz_title,
            date_of_quiz=date_of_quiz,
            time_duration=time_duration,
            remarks=remarks,
            chapter_id=chapter_id,
        )
        db.session.add(new_quiz)
        db.session.commit()
        flash("Quiz added successfully!", "success")
        return redirect("/admin/dashboard")
    return render_template("New Quiz.html", chapter=chapter)