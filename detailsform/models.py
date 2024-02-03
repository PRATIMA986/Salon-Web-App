from django.db import models
class details(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    # address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    # country=[('Afganistan', 'Afganistan'), ('India','India')]
    # country=models.CharField(max_length=50, choices=country)
    cname=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    yearofexperience=models.CharField(max_length=5)
        
 
# Create your models here.
    # country=models.Choices('Afganistan','India')
