from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = "stores"


class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    store = models.ForeignKey("Store", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "menus"

