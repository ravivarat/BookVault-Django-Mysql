from django.db import models

# Create your models here.
from django.db import models

# Admin Model
class Admin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Unique email to avoid duplicates
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


# Book Model
# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=100)
#     isbn = models.CharField(max_length=13, unique=True)
#     publication_date = models.DateField()
#     quantity = models.IntegerField()
#
#     def __str__(self):
#         return self.title
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()       # 📌 Published date field
    available = models.BooleanField(default=True)  # 📌 Availability field

    def __str__(self):
        return self.title