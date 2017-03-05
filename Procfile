web: python server.py
worker: celery beat --app=beckton.celery -B
worker: celery worker --app=beckton.celery -B
