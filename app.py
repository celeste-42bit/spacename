# ------------------------------------------
# fly_your_name_to_space
# app.py V.: 0.0.5
# https://github.com/celeste-42bit/spacename
# Copyright (C) 2022 celeste-42bit : MIT
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
    writeName(name)


@app.route("/page0")
def page0():
    return "Hello World!"


#TODO if file doesn't exist, create it and jump to write
#TODO if file exists, check if name already exists, if not write it
#TODO if file exists, check if name already exists, if yes, ask if user still wants to add it
def writeName(name):
    with open("names.txt", "r") as f:
        if f.readlines.__contains__(name):
            pass #TODO Page: Name already exists, u sure u want to add it?
        else:
            with open("names.txt", "a+") as f:  # Mode a+ creates the file "names.txt" if it does not exist and appends everything written.
                f.write(name + "\n")
                f.close()
        return render_template("done.html")


if __name__ == "__main__":
    app.run(debug=True)

