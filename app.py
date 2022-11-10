# ------------------------------------------
# send_your_name_to_space
# app.py V.: 0.0.0
# https://github.com/celeste-42bit/celestes-spacename
# Copyright (C) 2022 celeste-42bit
# ------------------------------------------

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html", "r")

@app.route("/page0")
def page0():
    return "Hello World!"