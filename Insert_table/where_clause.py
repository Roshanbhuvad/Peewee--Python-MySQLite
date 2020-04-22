import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:
		database = db
		db_table = 'notes'

#the example retrives all rows with ID greater than three

notes = Note.select().where(Note.id > 3)

#the where() methods applies a filtering condition on the query
for note in notes:
	print('{} {} on {}'.format(note.id, note.text, note.created))