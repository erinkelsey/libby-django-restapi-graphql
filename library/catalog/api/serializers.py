from rest_framework import serializers
from catalog.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ( 'first_name', 'last_name' )


class BookSerializer(serializers.ModelSerializer):
  author = AuthorSerializer(required=False)
  class Meta:
    model = Book
    fields = '__all__'
