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

	# in this program we are calling data of table name : notes of test2.db database which has mentioned in insert_many.py file, Once we typed python fetch_all.py in anaconda terminal then it will shows all data which is avaiolable in notes table of test2.db database