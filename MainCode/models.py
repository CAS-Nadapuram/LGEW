from django.db import models

# # Create your models here.

class Conductor(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, null=True)
    LastName = models.CharField(max_length=20, null=True)
    Contact = models.BigIntegerField(null=True)
    Place = models.CharField(max_length=20,null=True)
    Post = models.CharField(max_length=20, null=True)
    pin = models.BigIntegerField(null=True)
    Bus = models.CharField(max_length=20, null=True)

# class feedback(models.Model):
#     # User_id
#     Feedback = models.CharField(max_length=120)
#     Date = models.DateField()

# class login(models.Model):
#     UserId = models.AutoField(primary_key=True)
#     Username = models.CharField(max_length=25)
#     Password = models.CharField(max_length=25)
#     Type = models.CharField(max_length=25)

class Passenger(models.Model):
    UserId = models.AutoField(primary_key=True)
    LoginId = models.IntegerField()
    FirstName = models.CharField(max_length=20, null=True)
    LastName = models.CharField(max_length=20, null=True)
    Contact = models.BigIntegerField(null=True)
    Place = models.CharField(max_length=20, null=True)
    Post = models.CharField(max_length=20, null=True)
    pin = models.BigIntegerField(null=True)

# class Bank(models.Model):
#     # BankId = models.autoField(primary_key = True)
#     PassangerId = models.IntegerField()
#     AccountNumber = models.IntegerField()
#     IFSE_code = models.CharField(max_length=20)
#     Amount = models.IntegerField()

# class BusLocation(models.Model):
#     LocationId = models.IntegerField(primary_key=True)
#     BusId = models.IntegerField()
#     Latitude = models.FloatField()
#     Longitude = models.FloatField()

# class BusStop(models.Model):
#     StopId = models.AutoField(primary_key=True)
#     BusId = models.IntegerField()
#     stop = models.CharField(max_length=30)
#     Latitude = models.FloatField()
#     Longitude = models.FloatField()
#     TicketCharge = models.IntegerField()

# class Bustime(models.Model):
#     TimeId = models.IntegerField(primary_key=True)
#     StopId = models.IntegerField()
#     Time = models.CharField(max_length=30)
    
