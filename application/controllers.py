# this will have all the routes, redirect, etc will be here 

from flask import Flask, render_template, redirect, request

# app is defined in the app.py we have to import from app.py and import controller in app.py
# Also called circular import 

from flask import current_app as app # alias name as app

from .models import * # both resides in same folder


@app.route("/login", methods = ["GET", "POST"]) # URL wiht specific http method gives specific resource

def login():
    if request.method == "POST":
        return "logged in successfully"
    return render_template("Login Page.html")

@app.route("/register", methods = ["GET", "POST"])
def regiser():
    if request.method == "POST":
        return "Registered Successfully"
    return 


