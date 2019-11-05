#! /bin/sh
source env/bin/activate
python manage.py runserver
open -a Firefox http://127.0.0.1/experiment
