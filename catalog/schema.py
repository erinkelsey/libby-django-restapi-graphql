from graphene import relay, ObjectType, Mutation, Boolean, ID
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .api.serializers import BookSerializer, AuthorSerializer
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_file_upload.scalars import Upload
import boto3
import uuid

from .filters import BookFilter
from .models import Author, Book, BookImage


# AWS S3 Bucket
S3_BASE_URL = 's3.amazonaws.com'
BUCKET = 'libby-django-restapi-graphql'


class BookImageNode(DjangoObjectType):
  class Meta:
    model = BookImage


class BookNode(DjangoObjectType):
  class Meta:
    model = Book
    interfaces = (relay.Node, )


class AuthorNode(DjangoObjectType):
  class Meta:
    model = Author
    interfaces = (relay.Node, )
    # no filter
    filter_fields = []


class BookMutation(SerializerMutation):
  class Meta:
    serializer_class = BookSerializer


class BookImageMutation(Mutation):
  success = Boolean()

  class Arguments:
    file = Upload(required=True)
    id = ID(required=True)

  def mutate(self, info, file, **kwargs):
    photo_file = file
    book_id = kwargs.get('id')
    if photo_file and book_id:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind("."):]
      try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"https://{BUCKET}/{S3_BASE_URL}/{key}"
        photo = BookImage(url=url, book_id=book_id)
        photo.save()
      except Exception as e:
        print('Oops! There was a problem uploading the image: %s' % err)
        return BookImageMutation(success=False)
    else:
      print('Missing book ID or image file')
      return BookImageMutation(success=False)

    return BookImageMutation(success=True)


class Query(ObjectType):
  book = relay.Node.Field(BookNode)
  books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)
  author = relay.Node.Field(AuthorNode)
  authors = DjangoFilterConnectionField(AuthorNode)


class Mutation(ObjectType):
  book_mutation = BookMutation.Field()
  book_image_mutation = BookImageMutation.Field()