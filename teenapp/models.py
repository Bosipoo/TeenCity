from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class Teen(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    gender = models.CharField(max_length=20)
    dob = models.DateField(null=False)
    age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone= models.CharField(validators=[phone_regex], max_length=14, blank=True) 
    school = models.CharField(max_length=100)
    level = models.CharField(max_length=150)
    cclass = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    ambition = models.CharField(max_length=50)
    bornagain = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=150)