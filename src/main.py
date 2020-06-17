import logging

from flask import Flask, request, jsonify, abort

from src import config

app = Flask(__name__)


@app.route("/")
def home():
    return "Endpoints available: /surveys, /survey-responses"


@app.route("/surveys", methods=["GET", "POST"])
def surveys():
    if request.method == "POST":
        # create survey
        pass
    if request.method == "GET":
        # list all surveys
        pass


@app.route("/survey-responses", methods=["POST"])
def survey_responses():
    # create survey response
    pass


if __name__ == "__main__":
    app.run(debug=config.DEBUG, host=config.HOST)
