from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    subject=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title=models.CharField(max_length=40)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book_by_author')
    publish_date=models.DateField()
    ratings=models.FloatField()

    def __str__(self):
        return self.title
