#!/usr/bin/env bash
export FLASK_APP=run.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=configuration.py
flask run
