from flask import Flask, render_template, request

from app.model import TextMatcher
from app.train_data import archetypes

APP = Flask(__name__)
APP.matcher = TextMatcher(archetypes)


@APP.route("/", methods=["GET", "POST"])
def home():
    text = request.values.get("text", "")
    if text:
        return render_template(
            "home.html",
            result=APP.matcher(text),
            text=text,
        )
    else:
        return render_template("home.html")


if __name__ == '__main__':
    APP.run()
