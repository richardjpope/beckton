web: gunicorn beckton:app  --log-file -
worker: celery beat --app=beckton.celery -B
beat: celery worker --app=beckton.celery -B
