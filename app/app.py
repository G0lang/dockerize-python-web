from flask import Flask

# TODO: use create app method in flask 
# https://flask.palletsprojects.com/en/1.0.x/tutorial/factory/
application = Flask(__name__)


# root view 
# TODO: must be in seperate file view.py 
@application.route("/")
def hello():
    return "Hello World"

