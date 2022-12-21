from django.db import models

# Create your models here.
# Models are representations of tables in the database.
# "Code first approach" - create model and have application create table automatically based of class.

class Car(models.Model):
    make = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    

