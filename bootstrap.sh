#!/bin/sh

export FLASK_APP=./cashman/index.py
export FLASK_ENV=development

. venv/bin/activate

flask run -h 0.0.0.0
