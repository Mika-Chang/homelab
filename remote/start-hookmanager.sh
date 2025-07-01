#!/usr/bin/bash
#TODO: check for .venv dir and if flask app is running
source ../.venv/bin/activate
flask --app ./webhook_manager/app.py run &
./webhook_manager/hookdeck/hookdeck listen 5000 github-pages &
