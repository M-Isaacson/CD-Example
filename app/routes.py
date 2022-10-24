from flask import render_template
from app import app
from app.functions import check_name


@app.route("/")
def index():
    name = "David"
    user = check_name.is_valid_name(name)
    return render_template("index.html", name=name, user=user)
