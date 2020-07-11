from django.db import models
from django.conf import settings
from catalog.models import Book

# Create your models here.


class Review(models.Model):
  """Model definition for Review."""

  RATING_CHOICES = (
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
  )
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
  pub_date = models.DateField(auto_now_add=True, verbose_name='Publication Date')
  comment = models.TextField(max_length=1024)
  value = models.IntegerField(choices=RATING_CHOICES, default=5)

  class Meta:
    """Meta definition for Review."""
    
    verbose_name = 'Book Review'
    verbose_name_plural = 'Book Reviews'
    ordering = ['-pub_date']

  def __str__(self):
    """Unicode representation of Review."""

    return '{0}/{1} - {2}'.format(self.book.title, self.user.username, self.value)
