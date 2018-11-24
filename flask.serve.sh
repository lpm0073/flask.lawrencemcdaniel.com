#!/bin/sh
# McDaniel
# Nov 2018
#
# Usage:     Set environment environment variables for Flask
#
# Reference: http://flask.pocoo.org/docs/0.12/server/
#---------------------------------------------------------
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
