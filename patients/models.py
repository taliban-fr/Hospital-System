from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.patient_id