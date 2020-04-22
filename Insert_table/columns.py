import peewee
import datetime

#Inside the select() method, we can specify the names of the columns to be included in the query

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)
#The example includes two columns: text and created.

	class Meta:
		database = db
		db_table = 'notes'

#The Id is skipped. We limit the query to two instances.
notes = Note.select(Note.text, Note.created).limit(2)

output = [e for e in notes.tuples()]
print(output)

#The example includes two columns: text and created. The Id is skipped. We limit the query to two instances.

