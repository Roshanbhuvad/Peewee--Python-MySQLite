import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:
		database = db
		db_table = 'notes'
#we use two where expression combined with the & operator
notes = Note.select().where((Note.id > 2) & (Note.id < 6))

for note in notes:
	print('{} {} on {}'.format(note.id, note.text, note.created))