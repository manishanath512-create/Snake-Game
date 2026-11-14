from django.db import models
class StudentAdmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    course=models.CharField(max_length=50)
    address=models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
