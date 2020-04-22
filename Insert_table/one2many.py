import peewee
import datetime

db = peewee.SqliteDatabase('test.db')
#In the example we define two models that map to the tables. Then we select a customer and show his reservations.

class Customer(peewee.Model):

    name = peewee.TextField()

    class Meta:

        database = db
        db_table = 'customers'

class Reservation(peewee.Model):
	customer = peewee.ForeignKeyField(Customer, backref='reservations')
	"""A relationship between Customer and Reservation models is created with ForeignKeyField. 
	The backref attribute sets how we can refer to reservations from a customer."""
	created = peewee.DateField(default=datetime.date.today)

	class Mate:
		database = db
		db_table = 'reservations'

customer = Customer.select().where(Customer.name == 'Paul Novak').get()
#The customer instance has a property reservations, which contains the corresponding reservations.
for reservation in customer.reservations:
	print(reservation.id)
	print(reservation.created)