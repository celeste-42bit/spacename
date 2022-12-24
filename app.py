# ------------------------------------------
# fly_your_name_to_space
# app.py V.: 0.2.0
# https://github.com/celeste-42bit/spacename
# Copyright (C) 2022 celeste-42bit : MIT
# ------------------------------------------

from flask import Flask, render_template, redirect, url_for, request, send_from_directory, current_app, send_file
from pdfhandler import *
from PIL import Image, ImageDraw, ImageFont
import os, os.path


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"
ticket_writer = PdfTicketWriter('./uploads/ticket_original.pdf')

# route for main page + its function
@app.route("/")  # main page, loaded from index.html
def index():
    return render_template("index.html")


# extension of route "/" which accepts names
@app.route("/", methods=['POST'])  # Getting the name entered in the text field
def my_form_post():
    global name  # make name globally available
    name = request.form['text']
    writeName(name)
    return render_template("done.html")

#---------------------------------------------

@app.route("/ticket", methods=['GET', 'POST'])
def push_ticket():
    img = Image.open('./uploads/ticket_original.jpg')
    I1 = ImageDraw.Draw(img)
    I1.text((1960, 600), name, font = ImageFont.truetype('./static/arial-black.ttf', 40), fill=(50, 50, 50))
    img.show()
    img.save("./uploads/your-ticket.jpg")
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'your-ticket.jpg', as_attachment=True)

#---------------------------------------------


@app.route("/uploads/<path:filename>", methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


def writeName(name):
    with open("names.txt", "a+") as f:
        f.write(name + "\n")


if __name__ == "__main__":
    app.run(debug=True)


"""dumped pdf handling thingy...
@app.route('/do_make_ticket', methods=['GET','POST'])
def make_ticket(name = "Blubb"):
    # you will have to figure out x and y based on your ticket layout.
    x = 113.2
    y = 45.0

    ticket_writer.add_text(name, x, y, 12) # (str, x, y, size)
    bytes_file = ticket_writer.to_bytesio()
    ticket_writer.reload()

    return send_file(
        bytes_file,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'ticket-{name}.pdf'
    )
"""