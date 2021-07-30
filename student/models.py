from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Student(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','none')
    )
    gender=models.CharField(max_length=8,choices=gender_choice)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    phone_number=models.CharField(max_length=10)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','SouthSudanes'),
        ('5','Sudanes')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice)
    national_Id=models.CharField(max_length=20)
    email_address=models.EmailField()
    admission_date=models.DateField()
    medical_form=models.FileField()
    laptop_serial_number=models.CharField(max_length=4)
    academic_year=models.CharField(max_length=12)
    course_name=models.CharField(max_length=25)


