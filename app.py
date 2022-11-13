# ------------------------------------------
# send_your_name_to_space
# app.py V.: 0.0.0
# https://github.com/celeste-42bit/celestes-spacename
# Copyright (C) 2022 celeste-42bit
# ------------------------------------------

from flask import Flask, render_template, redirect, url_for, request
import os, os.path

app = Flask(__name__)

@app.route("/")  # main page, loaded from index.html
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])  # Getting the name entered in the text field
def my_form_post():
    name = request.form['text']
    with open("names.txt", "a+") as f:  # Mode a+ creates the file "names.txt" if it does not exist and appends everything written.
        f.write(name + "\n")
        f.close()
    return render_template("done.html")
    

@app.route("/page0")
def page0():
    return "Hello World!"