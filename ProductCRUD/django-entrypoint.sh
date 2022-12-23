#!/bin/bash

echo "Running migrations"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Run server"
gunicorn ProductCRUD.wsgi:application --bind 0.0.0.0:8000 --reload