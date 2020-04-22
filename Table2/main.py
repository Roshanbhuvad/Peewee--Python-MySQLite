from peewee import *
import datetime 

db = SqliteDatabase("data.db")

class Note(Model):
	content = TextField()
	timestamp = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database=db

if __name__ == '__main__':
	db.connect()
	db.create_tables([Note],safe=True)
	Note.create(content="new notes")