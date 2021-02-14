from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from auth.models import Profile


class WorkingShift(models.Model):
    day = models.ForeignKey('Days', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    login_time = models.CharField(max_length=10)
    logout_time = models.CharField(max_length=10)
    break_hours = models.ForeignKey(
        'BreakHours', on_delete=models.SET_NULL, null=True)


class Days(models.Model):
    day_name = models.CharField(max_length=10)


class BreakHours(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
