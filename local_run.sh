#! /bin/sh

if [ -d "pyenv" ] ;
then
    echo "Enabling virtual environment"
    . pyenv/bin/activate

else
    echo "No Virtual environment. Please set up it first"
    exit 1
fi

#Activate virtual environment
export ENV=development
python3 main.py
deactivate