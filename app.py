# ------------------------------------------
# fly_your_name_to_space
# app.py V.: 0.0.5
# https://github.com/celeste-42bit/spacename
# Copyright (C) 2022 celeste-42bit : MIT
# ------------------------------------------

from flask import Flask, render_template, redirect, url_for, request, send_from_directory, current_app
import os, os.path

app = Flask(__name__)

# route for main page + its function
@app.route("/")  # main page, loaded from index.html
def index():
    return render_template("index.html")

# extension of route "/" which accepts names
@app.route("/", methods=["POST"])  # Getting the name entered in the text field
def my_form_post():
    name = request.form['text']
    status = writeName(name)
    if(status == 0):
        return render_template("done.html") #TODO: This needs a download button
    else:
        return render_template("exists.html")

# Function for file download
@app.route("/download", methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    return send_from_directory(directory=uploads, filename=filename)


@app.route("/page0")
def page0():
    return "Hello World!"


def writeName(name):
    with open("names.txt", "a+") as f:
        if(f.readlines().__contains__(name)):
            return -1
        else:
            f.write(name)
            return 0


if __name__ == "__main__":
    app.run(debug=True)
