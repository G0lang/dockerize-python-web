from flask import Flask
application = Flask(__name__)


# root view 
# TODO: must be in seperate file
@application.route("/")
def hello():
    return "Hello World"

