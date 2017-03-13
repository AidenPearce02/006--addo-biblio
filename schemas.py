from marshmallow import ValidationError
from marshmallow import fields, validate, validates
from marshmallow_peewee import ModelSchema
from models import Author,Book
from marshmallow_peewee import Related


class AuthorSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(max=100)])
    birth_day = fields.Date()
    country = fields.Str(validate=[validate.Length(max=100)])
    class Meta:
        model = Author


class BookSchema(ModelSchema):
    title = fields.Str(validate=[validate.Length(max=100)])
    year = fields.Integer()
    author = Related(nested=AuthorSchema)

    class Meta:
        model = Book

    @validates('author')
    def validate_author(self, value):
        if not Author.filter(Author.id == value).exists():
            raise ValidationError("Can't find author")


author_schema = AuthorSchema()
book_schema = BookSchema()
