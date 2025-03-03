from flask import Flask, render_template,redirect,request
from flask import current_app as app #curret app refers to app.py 
from .models import * 

@app.route("/login",methods=["GET","POST"]) #url with specific http method gives specific results

def login():
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username=username).first() #LHS is column name RHS is the data fetched from the form in live server
        if this_user:
            if this_user.password == pwd:
                if this_user.type == "admin":
                    return render_template("Admin Dashboard.html",username=username) #LHS is jinja also linked in the admin dash and RHS is the data feched
                else:
                    return render_template("User Dashboard.html", username=username)
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