<img src="logo.png" alt="KSat logo" height="100" width="100" align="right"/>

# KSat spacename 1.1.5
Fly your name to space! Website based on Python-Flask (with templates for FARGO - for more, please open a request at the 'issues' section).

## Installation
Required: <br>
Python 3.8 or later (recommended: 3.11.0, tested for: 3.11, 3.10) <br>
https://docs.python.org/3/using/windows.html <br>
https://docs.python.org/3/using/unix.html <br>

Just use venv to creat a new virtual environment (env) for this project and then let pip install the requirements from the "requirements.txt" file.

Unix-likes/Linux: <br>
1. ```python -m venv env``` to create the virtual environment <br>
2. ```./env/Scripts/activate``` to activate the venv <br>
3. ```python -m pip install -r "requirements.txt"``` to download and install all the requirements. <br>

Windows: <br>
1. ```python.exe -m venv env``` <br>
2. ```.\env\Scripts\activate.ps1``` or ```.\env\Scripts\activate``` <br>
3. ```python.exe -m pip install -r "requirements.txt"```

## Run

To run the app, open a terminal inside the spacename folder and type: <br>
Unix-likes/Linux: <br>
```python -m app``` <br>
Windows: <br>
```python.exe .\app.py```
