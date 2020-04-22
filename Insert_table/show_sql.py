#The generated SQL statements can be shown with the sql() method.

import peewee
import datetime

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):
	text = peewee.CharField()
	created = peewee.DateField()

	class Meta():
		database = db
		db_table = 'notes'

note3 = Note.select().where(Note.id == 3)
print(note3.sql())

"""

O/P:
('SELECT "t1"."id", "t1"."text", "t1"."created" FROM "notes" AS "t1"
    WHERE ("t1"."id" = ?)', [3])