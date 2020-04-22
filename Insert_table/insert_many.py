import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:

		database = db
		db_table = 'notes'

Note.create_table()

data = [ # We define the data in a list of dictionaries

	{'text': "Tai chi in the morning", 'created': datetime.date(2018,10,20)},
	{'text': 'Visited friend', 'created':datetime.date(2018,10,12)},
	{'text':'Went to cinema', 'created':datetime.date(2018,10,5)},
	{'text':'Watched TV all day', 'created':datetime.date(2022,12,28)},
	{'text':'Worked in the garden', 'created':datetime.date(2019,11,25)},
	{'text':'Walked for a hour', 'created':datetime.date(2020,12,20)}
]


#We execute the bulk operation. The atomic() method puts the bulk operation in a transactio
with db.atomic():

	query = Note.insert_many(data)
	query.execute()