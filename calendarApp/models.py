from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calendar_id = models.CharField(max_length=50)

class Appointment(models.Model):
    title = models.CharField(max_length= 50, verbose_name= "Başlık")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()