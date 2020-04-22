import peewee
import datetime

# this below program creates a "notes" database table in SQLite
#We initiate a test.db SQLite database. This creates a test.db file on the filesystem
db = peewee.SqliteDatabase('test.db') 

#we define a database model called Note, Peewee model inherit from peewee.model
class Note(peewee.Model): 

#We specify the model fields,CharField is a field class for storing strings. DateField is a field class for storing date, It takes a default value if not specified
	text = peewee.CharField()
	created = peewee.DateTimeField(default=datetime.date.today)
#in the Meta class, We define the reference to the database and the database table name
	class Meta:
		database = db 
		db_table = 'notes'
#The table is created from a model with create_table()
Note.create_table()

note1 = Note.create(text='Went to the cinema')
note1.save() # We create and save a new instance

note2 = Note.create(text='Exercised in the morning',
		created=datetime.date(2020,4,21))
note2.save()

note3 = Note.create(text='Worked in the garden',
	craetd=datetime.date(2020, 4, 21))

note3.save()

note4 = Note.create(text='Listened to music')
note4.save()