#!/bin/sh

python /usr/src/app/manage.py collectstatic --noinput
python /usr/src/app/manage.py migrate
/usr/local/bin/gunicorn interlineapi.wsgi:application -w 2 -b :8000
