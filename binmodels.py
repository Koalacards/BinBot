from peewee import *

database = SqliteDatabase('bindata.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class GuildProperties(BaseModel):
    command_prefix = TextField(null=True)
    guild_id = AutoField()
    hourcooldown = IntegerField(null=True)
    thumbsdown = IntegerField(null=True)
    thumbsdownemoji = TextField(null=True)
    thumbsup = IntegerField(null=True)
    thumbsupemoji = TextField(null=True)

    class Meta:
        table_name = 'GuildProperties'

