from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DailyReport(models.Model):
    condition_choices = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
    ]

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    activity_choices = [
        ('little', 'Little'),
        ('moderate', 'Moderate'),
        ('too_much', 'Too much'),
    ]
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmr = models.DecimalField(max_digits=8, decimal_places=2)
    tdee = models.DecimalField(max_digits=8, decimal_places=2)
    total_calories = models.DecimalField(max_digits=8, decimal_places=2)
    calorie_difference = models.DecimalField(max_digits=8, decimal_places=2)
    body_condition = models.CharField(max_length=10, choices=condition_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    
    #Reports must keep the old user body info that used in calculating, 
    #Because UserBody model may update by user anytime.
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    gender = models.CharField(max_length=50, choices=gender_choices)
    physical_activity = models.CharField(max_length=50, choices=activity_choices)

    def __str__(self):
        return f'Report Code : DCT-R#{self.id} | For user {self.user.username}'



class FoodIntake(models.Model):
    unit_choices = [
        ('gram', 'Gram'),
        ('piece', 'Piece'),
        ('ml', 'Milliliter'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='foods', blank=True, null=True)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=10, choices=unit_choices)
    calories_per_unit = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Food intake #{self.id} | User : {self.user.username}'
