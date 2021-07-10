from django.db import models
import re
# Create your models here.

NAME_REGEX = re.compile(r"^[a-zA-Z-']+$")


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["title"] = "title name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "desc description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network name should be at least 3 characters"
        if len(postData['release_date']) < 10:
            errors["release_date"] = "please enter a valid release date"
        return errors






class Show(models.Model):
    network = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 255)
    release_date = models.DateField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



