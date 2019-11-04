#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

# python manage.py migrate
# python manage.py collectstatic --noinput --verbosity 0
# gunicorn config.wsgi -w 5 --worker-class gevent -b 0.0.0.0:5000 --chdir=/app
# gunicorn -w 5 --worker-class gevent 0.0.0.0:8000 --chdir=/app run:main

#ls -a
#echo $PWD
#python ./fridginator/wsgi.py --host=0.0.0.0 --port=8000
# gunicorn -w 5 -b 0.0.0.0:8000 --chdir=/app run:app
export FLASK_APP=app
export FLASK_ENV="development"
flask run --host=0.0.0.0 --port=8000 --with-threads
