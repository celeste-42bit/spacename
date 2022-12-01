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
    writeName(name)
    return render_template("done.html") #TODO: This needs a download button

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
        f.write(name + "\n")
        f.close()


#TODO if file doesn't exist, create it and jump to write
#TODO if file exists, check if name already exists, if not write it
#TODO if file exists, check if name already exists, if yes, ask if user still wants to add it

''' IDEAL, UN-OPTIMIZED
def writeName(name):  # TODO optimize!
    if os.path.exists("./names.txt"):
        with open("names.txt", "ra+") as f:  # TODO is ra+ valid???
            if f.readlines.__contains__(name):
                pass # TODO ask if user wants to write
            else:
                f.write(name)
    else:
        with open("names.txt", "a+") as f:
            f.write(name)
            f.close()
'''


''' PRE
def writeName(name):
    with open("names.txt", "r") as f:
        if f.readlines.__contains__(name):
            pass #TODO Page: Name already exists, u sure u want to add it?
        else:
            with open("names.txt", "a+") as f:  # Mode a+ creates the file "names.txt" if it does not exist and appends everything written.
                f.write(name + "\n")
                f.close()
        return render_template("done.html")
'''

if __name__ == "__main__":
    app.run(debug=True)
