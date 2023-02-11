#!/bin/bash

export DJANGO_SETTINGS_MODULE=Silant.settings

python manage.py makemigrations app
python manage.py makemigrations users
python manage.py makemigrations manuals
python manage.py migrate
python init_db.py