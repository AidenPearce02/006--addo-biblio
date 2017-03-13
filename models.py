import peewee as pw

db = pw.SqliteDatabase('database.db')


def initialize():
    Author.create_table(fail_silently=True)
    Book.create_table(fail_silently=True)


class BaseModel(pw.Model):
    class Meta:
        database = db


class Author(BaseModel):
    name = pw.CharField(max_length=100)
    birth_day = pw.DateField()
    country = pw.CharField(max_length=100)


class Book(BaseModel):
    title = pw.CharField(max_length=100)
    year = pw.IntegerField()
    author = pw.ForeignKeyField(Author)
