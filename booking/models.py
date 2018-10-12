from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Screen(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return "Screen: {}".format(self.name)


@python_2_unicode_compatible
class Seat(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey(Screen, related_name="seats")
    
    def __str__(self):
        return "Seat: {}".format(self.title)
