from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserBody(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    activity_choices = [
        ('little', 'Little'),
        ('moderate', 'Moderate'),
        ('too_much', 'Too much'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    gender = models.CharField(max_length=50, choices=gender_choices)
    physical_activity = models.CharField(max_length=50, choices=activity_choices)

    def __str__(self):
        return f'User body info ID : #{self.id} | {self.user.username}'
    
    class Meta:
        verbose_name_plural = 'Users body info'