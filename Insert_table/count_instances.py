#To calculate the number of model instances in the table, we can use the count() method.
import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField(default=datetime.date.today)

	class Meta:
		database = db
		db_table = 'notes'

	n = Note.select().count()
	print(n)

	n2 = Note.select().where(Note.created >= datetime.date(2018, 10, 20)).count()
	print(n2)

	"""The example counts the number of all instances and 
	the number of instances where the date is equal or later than 2018/10/20.

	O/P:
	7
	4 """

