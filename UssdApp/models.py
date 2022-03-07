import email
from operator import mod, truth
from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    phoneNumber = models.CharField(max_length=15, null=True)
    firstName = models.CharField(max_length=65, null=True)
    secondName = models.CharField(max_length=65, null=True)
    email = models.EmailField()
    city = models.CharField(max_length=65, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(null=True)

    def __str__(self):
        return self.phoneNumber




class AppartmentLocation(models.Model):
    locationName = models.CharField(max_length=65, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.locationName



class Booking(models.Model):
    user = models.CharField(max_length=65, null=True)
    phoneNumber = models.CharField(max_length=65, null=True)
    num_of_people = models.IntegerField(null=True, default=0)
    num_of_adults = models.IntegerField(null=True, default=0)
    num_of_children = models.IntegerField(null=True, default=0)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(auto_now_add=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    
 
    def __str__(self):
        return self.user



class session_levels(models.Model):
	session_id = models.CharField(max_length=25,primary_key=True)
	phonenumber= models.CharField(max_length=25,null=True)
	level = models.IntegerField(null=True)
