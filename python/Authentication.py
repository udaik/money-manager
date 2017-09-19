from pymodm import EmbeddedMongoModel, fields

class AuthInfo(EmbeddedMongoModel):
    username = fields.CharField()
    password = fields.CharField()
