from datetime import datetime
from mongoengine import Document, StringField, IntField, DateTimeField, signals
from securemongoengine.fields import *
from beckton import tasks
from beckton import app

_key = app.config['DATABASE_ENCRYPTION_KEY']

class Commitment(Document):
    name = EncryptedStringField(key=_key, max_length=100, required=True)
    mobile_number = EncryptedStringField(key=_key, required=True, max_length=20, unique=True)
    rate = IntField(required=True)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        if kwargs.get('created', False):
            tasks.send_committed_message.delay(document.mobile_number)

class Milestone(Document):
    name = StringField(max_length=50, required=True)
    created_at = DateTimeField(default=datetime.now)

signals.post_save.connect(Commitment.post_save, sender=Commitment)