from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    """Returns text welcome"""
    return "welcome"

@app.get("/welcome/home")
def welcome_home():
    """Returns text welcome home"""
    return "welcome home"

@app.get("/welcome/back")
def welcome_back():
    """Returns text welcome back"""
    return "welcome back"

