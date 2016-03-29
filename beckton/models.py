from mongoengine import Document, StringField, signals
from securemongoengine.fields import *
from beckton import tasks

class Commitment(Document):
    name = EncryptedStringField(max_length=100, required=True)
    mobile_number = EncryptedStringField(required=True, max_length=20, unique=True)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        if kwargs.get('created', False):
            tasks.send_committed_message(document)



    def __init__(self, key, *args, **kwargs):
        super(Commitment, self).__init__(*args, **kwargs)
        for k,v in self._fields.iteritems():
            if type(v) in [EncryptedStringField]:
                v.key = key

signals.post_save.connect(Commitment.post_save, sender=Commitment)