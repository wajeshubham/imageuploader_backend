web: gunicorn uploader_bknd.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate