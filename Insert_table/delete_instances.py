import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'
       

query = Note.delete().where(Note.id > 3)
n = query.execute()

print('{} instances deleted'.format(n))

#In the example, we delete all instances with Id greater than three.

"""
4 instances deleted
In our case, we have deleted four Note instances"""