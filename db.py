from peewee import *

db = SqliteDatabase('mydb.db3')

class Frase(Model):
    text = TextField(unique=True)
    answer = TextField()

    class Meta:
        database = db
        indexes = ['text']
        order_by = ['text']

class Settings(Model):
    name = TextField(unique=True)
    value = TextField()

    class Meta:
        database = db
        indexes = ['name']
        order_by = ['name']

Frase.create_table()
Settings.create_table()