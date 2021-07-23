from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=12)
    nationality = models.CharField(max_length=20)
    email_address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=13)
    health_status = models.CharField(max_length=50)
    # profile_picture = models.ImageField()
    guardian_full_name = models.CharField(max_length=32)
    class_name = models.CharField(max_length=8)
    passport_number = models.CharField(max_length=13)
    academic_year  = models.CharField(max_length=4)
    admission_date = models.DateField()


