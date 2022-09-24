# Note if one day your static files in the folder can't  be readed or ur css has problem, then just
# hard Refresh the page by (ctrl + shift + R)
import json
from requests.exceptions import HTTPError

import werkzeug
from flask import Flask, request, render_template, url_for, Response, redirect, session
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase


# cred = credentials.Certificate("serviceAccountKey.json");
# n.initialize_app()

cred = credentials.Certificate('serviceAccountKey.json')
firebaseAuth = firebase_admin.initialize_app(cred, name = "firebaseAuth")
firebase = pyrebase.initialize_app(json.load(open("config.json")))
Auth = firebase.auth();

adminAuth = firebase_admin.initialize_app(cred)


# if (__name__ == "__main__"): 
    
app = Flask(__name__)



@app.errorhandler(werkzeug.exceptions.HTTPException)
def handleBadRequest(e) :
    
    response = e.get_response();
    response.data = json.dumps({
        "code" : e.code,
        "name" : e.name,
        "description" : e.description
    })
    response.content_type = "application/json"
    return response

@app.route('/home')
def Home():
    return render_template("home.html", title = "After Login", email = session["Email"], password = session["Password"]);

@app.route("/Logout") 
def Logout() :
    session.pop('Email')
    session.pop('Password')
    return redirect(url_for("Login"));

@app.route("/Login", methods=['POST', 'GET'])
def Login(): 
    if request.method == 'GET':
        return render_template("base.html", Header = "Login", buttonText = "Login")
    elif request.method == "POST" :
        print("INI masuk")
        Email = request.form['email'];
        Password = request.form['pass'];
        try :
            User = Auth.sign_in_with_email_and_password(Email, Password);
        except HTTPError :
            return "<h1>Error your Email or password is invalid</h1>";


        if User :
            session["Email"] = Email;
            session["Password"] = Password;
            return redirect(url_for("Home")) 
        
@app.route('/SignUp', methods = ["GET", "POST"])
def SignUp():
    if request.method == "GET" :
        return render_template("base.html", Header = 'Sign Up', buttonText = "Sign UP", url = request.path);
    if request.method == "POST" :
        rEmail = request.form['email']
        rPassword = request.form['pass'];

        user = auth.create_user(
            email = rEmail,
            password = rPassword
        )
        return redirect(url_for('Login'));

@app.route("/index/")
def index():
    return "Hellow World, this is from page Index"

@app.route("/")
def notFOund():
    return redirect('Login')
    
    



if __name__ == "__main__" :
    app.secret_key = "myServer"
    app.run(debug=True);
    
    # use the Url for static when your file name or folder name aren't "static" anymore
    # url_for('static', filename='static')