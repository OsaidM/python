from django.db import models
import re
# Create your models here.
NAME_REGEX = re.compile(r"^[a-zA-Z-']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    def register_validator(self,postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if user:
            errors['email'] = "there is already a user with this email address"
            return errors
        if len(postData['fname']) < 1:
            errors['fname'] = 'first name is required'
        if len(postData['lname']) < 1:
            errors['lname'] = 'last name is required'
        if len(postData['fname']) < 3:
            errors['fname'] = 'first name should be at least 3 characters'
        if len(postData['lname']) < 3:
            errors['lname'] = 'last name should be at least 3 characters'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'please enter a valid email'
        if not NAME_REGEX.match(postData['fname']):
            errors['fname'] = 'please enter a valid first name'
        if not NAME_REGEX.match(postData['lname']):
            errors['lname'] = 'please enter a valid last name'

        if len(postData['pwd']) < 8:
            errors['pwd'] = 'password should be at least 8 characters'
        if postData['pwd'] != postData['cpwd']:
            errors['cpwd'] = 'Your password confirmation does not match your password.'
        
        if len(errors) > 0:
            return errors
        else:
            user = User.objects.create(first_name= postData['fname'],last_name= postData['lname'],email= postData['email'],password= postData['pwd'])
            return (True, user)
    def login_validator(self, postData):
        user = User.objects.filter(email = postData['email'])
        if user:
            errors['email'] = "there is already a user with this email address"
            return errors
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'please enter a valid email'





class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length= 255)
    uploaded_buy = models.ForeignKey(User, related_name='books_uploaded', on_delete= models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = 'liked_books')
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)