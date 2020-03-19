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
import json

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

logging.info("python code started")


@app.route("/v1")
def working():
    return {"response": "api gateway service running"}


@app.route("/v1/otp", methods=["GET"])
def otp():
    response = requests.get("http://127.0.0.1:7002/v1/otp", params=request.args)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/otp/verify", methods=["GET"])
def otp_verify():
    response = requests.get("http://127.0.0.1:7002/v1/otp/verify", params=request.args)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/createuser", methods=["POST"])
def createuser():
    response = requests.post("http://127.0.0.1:7002/v1/createuser", data=request.form)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/login", methods=["GET"])
def login():
    response = requests.get("http://127.0.0.1:7002/v1/login", params=request.args)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/book", methods=["POST"])
def book():
    response = requests.post("http://127.0.0.1:7004/v1/book", data=request.form, headers=request.headers)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/cancel", methods=["POST"])
def cancel():
    response = requests.post("http://127.0.0.1:7004/v1/cancel", data=request.form, headers=request.headers)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/fare", methods=["GET"])
def fare():
    response = requests.get("http://127.0.0.1:7004/v1/fare", params=request.args, headers=request.headers)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/endTrip", methods=["POST"])
def endTrip():
    response = requests.post("http://127.0.0.1:7004/v1/endTrip", data=request.form, headers=request.headers)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/getDistance", methods=["GET"])
def getDistance():
    response = requests.get("http://127.0.0.1:7004/v1/getDistance", params=request.args, headers=request.headers)
    return Response(response=response.content, headers=dict(response.headers))


@app.route("/v1/bookingPath", methods=["GET"])
def bookingPath():
    response = requests.get("http://127.0.0.1:7004/v1/bookingPath", params=request.args, headers=request.headers)
    return Response(response=response.content, headers=dict(response.headers))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=443, ssl_context='adhoc')
