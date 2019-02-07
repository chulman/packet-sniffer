!#/bin/bash

pip install Django && cd /home/docker/code python manage.py makemigrations && python manage.py migrate && gunicorn mydjango.wsgi -b 0.0.0.0:8000