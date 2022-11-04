#!/bin/sh
export FLASK_APP=./thatvacay/example.py
pipenv run flask --debug run -h 0.0.0.0