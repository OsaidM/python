from django.db import models
import re
import bcrypt

NAME_REGEX = re.compile(r"^[a-zA-Z-']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["eml"] = "title name should be at least 5 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "title name should be at least 5 characters"
        if len(postData['eml']) < 5:
            errors["eml"] = "email name should be at least 5 characters"
        if len(postData['pwd']) < 8:
            errors["pwd"] = "password should be at least 8 characters"
        return errors

    def login(self, postData):
        errors = []
        
        if len(postData['leml']) < 1 or len(postData['lpwd']) < 1:
            errors.append("All entries must be filled in!")
        elif len(postData['lpwd']) < 8:
            errors.append("Password should be at least 8 characters")
        elif not EMAIL_REGEX.match(postData['leml']):
            errors.append("Invalid Email Address")
        
        check_emails = User.objects.filter(email = postData['leml'])
        if len(check_emails) == 0:
            errors.append("Email does not exist")
            return (False, errors)
        else:
            user = check_emails[0]
            if len(errors) > 0:
                return (False, errors)
            else: 
                return(True, user)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()