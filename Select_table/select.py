import peewee
import datetime
#The example fetches and displayes all Note instances
db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:

		 database = db
		 db_table = 'notes'
# the select() method create a SELECT query, If no field are explicitly provided, the query will be default select all the filds defined on the model

notes = Note.select()

for note in notes:
	print('{} on {}'.format(note.text, note.created))