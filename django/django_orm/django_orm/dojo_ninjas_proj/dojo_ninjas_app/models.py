from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    desc = models.TextField(null=True)
    state = models.CharField(max_length = 2)

class ninjas(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    ninja = models.ForeignKey(Dojos, related_name='ninjas', on_delete = models.CASCADE)