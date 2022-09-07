from django.db import models
class Manufacturer(models.Model):

    pass

class Car(models.Model):
    manufacturer = models.ForeingKey(Manufacturer, on_delete=models.CASCADE)



class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)


class Place(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name
class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.Boolean_Field(default=False)
    serves_pizza = models.Boolean_Field(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name