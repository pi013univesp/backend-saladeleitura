from django.db import models
    
class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=100)
    library_fk = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        blank=True, null=True
    )


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    tombo = models.DateTimeField(blank=True, null=True)
    procedencia = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)


class Books_at_library(models.Model):
    id = models.AutoField(primary_key=True)
    library_fk = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
    )
    book_fk = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
    )
    book_stock = models.IntegerField()
    number_of_borrowed_books = models.IntegerField(default=0)


class Borrow(models.Model):
    id = models.AutoField(primary_key=True)
    book_fk = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    client_fk = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )
    library_fk = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
    )
    borrow_date = models.DateTimeField()
    end_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    forum = models.IntegerField()
    name = models.CharField(max_length=100)
    commentText = models.CharField(max_length=2000)
