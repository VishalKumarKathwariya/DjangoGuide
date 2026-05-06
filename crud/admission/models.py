from django.db import models

# Create your models here.
class Admission(models.Model):
        GENDER = [('Male','Male'),('Female','Female'),('Other','Other')]
        COURSE = [('BCA','BCA'),('BBA','BBA'),('BTech','BTech')]

        name = models.CharField(max_length=100)
        father_name = models.CharField(max_length=100)
        dob = models.DateField()
        gender = models.CharField(max_length=10, choices=GENDER)

        email = models.EmailField(unique=True)
        phone = models.CharField(max_length=10)
        address = models.TextField()

        course = models.CharField(max_length=20, choices = COURSE)
        previous_school = models.CharField(max_length=200)
        marks = models.FloatField()

        photo = models.ImageField(upload_to='photos/')
        signature = models.ImageField(upload_to='signatures/')
        document = models.ImageField(upload_to='documents/')

        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.name 