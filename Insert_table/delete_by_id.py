#The delete_by_id() method deletes an instance identified by its Id. It returns the number of deleted instances.

import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'

n2 = Note.delete_by_id(1)
print(n2)