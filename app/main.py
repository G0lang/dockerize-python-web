from flask import Flask
app = Flask(__name__)


# root view 
# TODO: must be in seperate file
@app.route("/")
def hello():
    return "Hello World"


# TODO: we have to get debug mode from ENV 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
