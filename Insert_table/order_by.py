import peewee
import datetime

#The retrieved instances can be ordered with order_by(), It means print the data in Ascending and Descending ordered

db = peewee.SqliteDatabase('test2.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db 
        db_table = 'notes'
#The code example orders the instances by the date of creation.

print("Ascending Order")
print("**************************")
#This line returns the note instances ordered by creation date in ascending order.
notes = Note.select(Note.text, Note.created).order_by(Note.created)

for note in notes:
	print(note.text, note.created)
print()

print("Descending Order")
pritn("******************************")
#To retrieve the notes in ascending order, we append the desc() method on the field.
notes = Note.select(Note.text, Note.created).order_by(Note.created.desc())

for note in notes:
	print(note.text, note.created)

#This is the ordered list of note instances.

