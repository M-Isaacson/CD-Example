from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "I'm sorry. This app is just about testing some github actions."
