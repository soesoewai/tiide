from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/soe")
def soe():
    return "Hello Soe Soe Wai"
