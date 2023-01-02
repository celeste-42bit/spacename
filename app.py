# ------------------------------------------
# fly_your_name_to_space
# app.py V.: 1.0.0
# https://github.com/celeste-42bit/spacename
# Copyright (C) 2022 celeste-42bit : MIT
# ------------------------------------------

from flask import Flask, render_template, redirect, url_for, request, send_from_directory, current_app, send_file
from PIL import Image, ImageDraw, ImageFont
import os, os.path


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"

# route for main page + its function
@app.route("/")  # main page, loaded from index.html
def index():
    return render_template("index.html")

#---------------------------------------------- User input & name > names.txt

# extension of route "/" which accepts names
@app.route("/", methods=['POST'])  # Getting the name entered in the text field
def my_form_post():
    global name
    name = request.form['text']
    writeName(name)
    return render_template("done.html")

#---------------------------------------------- Ticket creation

@app.route("/ticket", methods=['GET', 'POST'])
def push_ticket():
    img = Image.open('./uploads/ticket_original.jpg')
    I1 = ImageDraw.Draw(img)

    # text generation and placement
    I1.text((1960, 610), name, font = ImageFont.truetype('./static/calibri.ttf', 40), fill=(50, 50, 50))

    #img.show() # this line displays the image on the client right after creation
    img.save("./uploads/your-ticket.jpg")  # synchronously overwrites the "old" ticket every time a new one is created
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'your-ticket.jpg', as_attachment=True)

#----------------------------------------------


@app.route("/uploads/<path:filename>", methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


def writeName(name):
    with open("names.txt", "a+") as f:
        f.write(name + "\n")


if __name__ == "__main__":
# "deployed mode", posting on all interfaces, port 80, debug disabled (WARNING: Debug mode is not safe for deployment!)
    app.run(host='0.0.0.0', port=80, debug=False)

# "debug mode" on localhost:5000 (debug mode allows for quick server updates, every time changes to the code are saved by [CTRL]+[S])
    #app.run(debug=True)
