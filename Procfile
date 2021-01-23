web: gunicorn uploader_bknd.wsgi:application --timeout 15 --keep-alive 5 --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate