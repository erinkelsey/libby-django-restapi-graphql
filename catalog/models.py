from django.db import models


# Create your models here.
class Book(models.Model):
  """Model definition for Book."""

  title = models.CharField(max_length=200)
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
  summary = models.TextField(max_length=1000, help_text="Enter a brief description.", blank=True)

  class Meta:
    """Meta definition for Book."""
    ordering = ['-id'] 
    verbose_name = 'Book'
    verbose_name_plural = 'Books'

  def __str__(self):
    """Unicode representation of Book."""
    return self.title


class Author(models.Model):
  """Model definition for Author."""

  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  class Meta:
    """Meta definition for Author."""

    ordering = ['last_name', 'first_name']
    verbose_name = 'Author'
    verbose_name_plural = 'Authors'

  def __str__(self):
    """Unicode representation of Author."""
    return f'{self.last_name}, {self.first_name}'


class BookImage(models.Model):
  """Model definition for MODELNAME."""

  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  url = models.CharField(max_length=255)

  class Meta:
    """Meta definition for BookImage."""

    verbose_name = 'Book Image'
    verbose_name_plural = 'Book Images'

  def __str__(self):
    """Unicode representation of BookImage."""
    return self.book.title
