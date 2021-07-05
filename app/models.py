from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    