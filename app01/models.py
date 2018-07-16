from django.db import models
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 32,unique=True)
    price = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    publish = models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
    pub_date = models.DateField()
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ad = models.OneToOneField(to="Ad",to_field="id" ,on_delete = models.CASCADE)

class Ad(models.Model):
    gf = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)

