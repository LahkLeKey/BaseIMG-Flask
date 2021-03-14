from flask import Flask

api = Flask(__name__)

@api.route("/")
def root():
    return "Hello from BaseIMG-Flask"
