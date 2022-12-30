#!/bin/bash
echo "Creating virtual environment 'env' using python-venv, this might take a second..."
python -m venv env
./env/scripts/activate.sh
echo "Installing all neccessary components for spacename on your server!"
python -m pip install -r ./requirements.txt
python -m pip install --upgrade pip
echo "Done! - Press [ENTER] to quit."
read $0
exit 0
