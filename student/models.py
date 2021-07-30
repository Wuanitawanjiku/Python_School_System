from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    gender_choice = ((u'F',u'female'),(u'M',u'male'),(u'O',u'other'))
    gender = models.CharField(max_length=12, choices=gender_choice)
    phone_number = models.CharField(max_length=13)
    health_status = models.CharField(max_length=50)
    email_address = models.CharField(max_length=40)
    guardian_full_name = models.CharField(max_length=32)
    guardian_email = models.EmailField()
    guardian_phone_number = models.CharField(max_length=12)
    admission_date = models.DateField()
    nationality = models.CharField(max_length=20)   
    # profile_picture = models.ImageField()    
    class_name = models.CharField(max_length=8)
    passport_number = models.CharField(max_length=13)
    academic_year  = models.CharField(max_length=4)
    admission_date = models.DateField()


