from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World My name is derrick. Welcome to my website. Please do add /login to the end of the url to begin :)'

@app.route("/login")
def login():
   return render_template("home.html")

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/cybercrimes")
def cybercrimes():
   return render_template("CyberCrimes.html")

@app.route("/3cat")
def categories():
   return render_template("3catcybercrimes.html")
   
@app.route("/precautions")
def precautions():
   return render_template("precautions.html")

@app.route("/malware")
def malware():
   return render_template("whattodo.html")
   
@app.route("/questionnaire")
def questionnaire():
   return render_template("questionnaire.html")
   
@app.route("/form")
def form():
   return render_template("form.html")

@app.route("/thankyou")
def thanks():
   return render_template("thankyou.html")

if __name__ == '__main__':
    app.run(debug=True)   