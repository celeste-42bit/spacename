# KSat spacename
Fly your name to space! Website based on Python-Flask.

## A friendly warning ⚠
This is not a production version but rather a prototype of the website, intended for demonstration purposes only. <br>
In its current state it is NOT SAFE TO USE on a host platform! <br> <br>
Do NOT press the download button on the /done page, unless you wanna make the program crash. It's not implemented yet and there is nothing catching the error. No damage will be done, but - try at your own risk HEHE ^^

## Installation
Required: <br>
Python 3.8 or later (3.11.0 is recommended) <br>
https://docs.python.org/3/using/windows.html <br>
https://docs.python.org/3/using/unix.html <br>

Just use venv to creat a nev virtual environment for this project and then let pip install the requirements from the requirements.txt file.

Unix-likes/Linux: <br>
1. ```python -m venv env``` to create the virtual environment <br>
2. ```./env/Scripts/activate``` to activate the venv <br>
3. ```python -m pip install -r requirements.txt``` to download and install all the requirements. <br>

Windows: <br>
1. ```python.exe -m venv env``` <br>
2. ```.\env\Scripts\activate.ps1``` or ```.\env\Scripts\activate``` <br>
3. ```python.exe -m pip install -r requirements.txt```

## Run

To run the app, open a terminal inside the spacename folder and type: <br>
Unix-likes/Linux: <br>
```python ./app.py``` <br>
Windows: <br>
```python.exe .\app.py```

## Deployment

Comming soon! <br>
We're still working on a deployment package, which will run the webserver via nginx with the help of python-gunicorn. <br>
As sson as we are done, we'll post the install instructions right here ^^

## Notes

So I know the boilerplate HTML code is very whacky and I will use some jinja at a later point in time to implement CSS formatting and modular HTML integrations to make all of this look a lot sexier!

The download function is still on its way to be integrated and I'm just playing around with it to check out how it works. For now, this should be enough for a little presentation. Have fun with it and pls don't hit me for any bugs you may find ^^