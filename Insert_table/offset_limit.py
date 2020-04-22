"""With the offset and limit attributes we can define the initial skip of instances and 
number of instances to be included in the select()."""

import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default = datetime.date.today)

	class Meta:
		database = db
		db_table = 'notes'

notes = Note.select().offset(2).limit(3)

for note in notes:
	print(note.id, note.text, note.created)

#The example returns three instances, starting from the second instance.
""" Output :
3 Went to cinema 2018-10-05
4 Listened to music 2018-10-28
5 Watched TV all day 2018-10-14	
"""