#!/bin/sh
export FLASK_APP=./thatvacay/verysimple.py
pipenv run flask --debug run -h 0.0.0.0