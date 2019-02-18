#!/bin/bash

set -e


echo -e '\n\n\033[34;1mActivating virtualenv...\033[0m'
source venv/bin/activate


echo -e '\n\n\033[34;1mApplying any new migrations...\033[0m'
./manage.py migrate


echo -e '\n\n\033[34;1mRunning the server...\033[0m'
./manage.py runserver
