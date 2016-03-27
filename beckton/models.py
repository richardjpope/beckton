from mongoengine import Document, StringField
from securemongoengine.fields import *

class Commitment(Document):
    name = EncryptedStringField(max_length=100, required=True)
    mobile_number = EncryptedStringField(required=True, max_length=20, unique=True)

    def __init__(self, key, *args, **kwargs):
        super(Commitment, self).__init__(*args, **kwargs)
        for k,v in self._fields.iteritems():
            if type(v) in [EncryptedStringField]:
                v.key = key