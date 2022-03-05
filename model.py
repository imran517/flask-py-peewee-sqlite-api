
from dbContext import db
from peewee import *

class BaseModel(Model):
    class Meta:
        database = db
        table_name = 'task'

class Task(BaseModel):
    id = AutoField()
    name = CharField()
    description= CharField()
    priority = CharField()
    status= CharField()

