import peewee
import datetime
#the example shows how to retrieve a single instance(Table data according to table colums name) in two ways
db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:
		database = db
		db_table = 'notes'
#We can use the chain of Note.select().where().get() methods
note1 = Note.select().where(Note.text =='Went to cinema').get()
print(note1.id)
print(note1.text)
print(note1.created)

#there is also a Note.get() shortcut method, which does the same
note2 = Note.get(Note.text == 'Walked for a hour')

print(note2.id)
print(note2.text)
print(note2.created)


"""
output: 
3
Went to cinema
2018-10-05
6
Walked for a hour
2020-12-20
"""