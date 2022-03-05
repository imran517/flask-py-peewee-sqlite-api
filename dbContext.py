from config import config
from peewee import *

db = SqliteDatabase(config.db.name())


