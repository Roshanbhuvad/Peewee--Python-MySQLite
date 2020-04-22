import peewee
import datetime

db = peewee.SqliteDatabase('test1.db')

class Unique(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:
		database = db
		db_table = 'uniques'

Unique.create_table()

unique1 = Unique.create(text="Went to the cinema")
unique1.save()

unique2=Unique.create(text="I am going to study",
		created=datetime.date(2019,10,22))
unique2.save()

# If we run this code We didn't see the table data and even table name because of Unique.drop_table() syntax
Unique.drop_table() 