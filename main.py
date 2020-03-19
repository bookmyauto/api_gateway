"""
    Description:    This code is the api gateway exposed to user side  app
    Author:         Rahul Tudu
"""
from flask import make_response
from    flask   import Flask
from    flask   import Response
from    flask   import request
import  logging
import  requests
import  ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

logging.info("python code started")


def arrange(response):
    with app.app_context():
        res = make_response(response.json())
    for key, value in response.headers.items():
        res.headers[key] = value
    return res


@app.route("/v1")
def working():
    return {"response": "api gateway service running"}


@app.route("/v1/otp", methods=["GET"])
def otp():
    return arrange(requests.get("http://127.0.0.1:7002/v1/otp", params=request.args))


@app.route("/v1/otp/verify", methods=["GET"])
def otp_verify():
    return arrange(requests.get("http://127.0.0.1:7002/v1/otp/verify", params=request.args))


@app.route("/v1/createuser", methods=["POST"])
def createuser():
    return arrange(requests.post("http://127.0.0.1:7002/v1/createuser", data=request.form))


@app.route("/v1/login", methods=["GET"])
def login():
    return arrange(requests.get("http://127.0.0.1:7002/v1/login", params=request.args))


@app.route("/v1/book", methods=["POST"])
def book():
    return arrange(requests.post("http://127.0.0.1:7004/v1/book", data=request.form, headers=request.headers))


@app.route("/v1/cancel", methods=["POST"])
def cancel():
    return arrange(requests.post("http://127.0.0.1:7004/v1/cancel", data=request.form, headers=request.headers))


@app.route("/v1/fare", methods=["GET"])
def fare():
    return arrange(requests.get("http://127.0.0.1:7004/v1/fare", params=request.args, headers=request.headers))


@app.route("/v1/endTrip", methods=["POST"])
def endTrip():
    return arrange(requests.post("http://127.0.0.1:7004/v1/endTrip", data=request.form, headers=request.headers))


@app.route("/v1/getDistance", methods=["GET"])
def getDistance():
    return arrange(requests.get("http://127.0.0.1:7004/v1/getDistance", params=request.args, headers=request.headers))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=443, ssl_context='adhoc')
