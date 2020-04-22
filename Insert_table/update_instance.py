#The update() method updates an instance. It returns the number of successfully updated instances.
import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'

query = Note.update(created=datetime.date(2018,10,27)).where(Note.id == 1)
n = query.execute()
print('# of row updated: {}'.format(n))

#The example modifies the creation date of the note with Id 1.