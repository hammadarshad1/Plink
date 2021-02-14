from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ProfileType(models.Model):
    """
    profile type will be the:
        - patient
        - doctor
        - admin
        ...
    """
    profile_type = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    speciality = models.ForeignKey(
        'Speciality', on_delete=models.CASCADE, null=True, blank=True)
    profile_type = models.ForeignKey(ProfileType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def full_name(self):
        """
        to get the full name of user
        because django default User
        object have 2 fields for name
            - first_name
            - last_name
        
        @return:
            - full_name (str): first_name + last_name
                e.g.
                    - first_name => Muhammad
                    - last_name => Hammad
                    - full_name => Muhammad Hammad
        """
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        """
        to set the default str for
        django admin so admin can 
        see which record is for e.g.
            - Doctor - Muhammad Hammad
            - Patient - Usman Aqil
        """
        return f'{self.speciality.specialitye} - {self.full_name}'


class Speciality(models.Model):
    """
    speciality will be the:
        - neurosurgeon
        - physiotherapist
        ...
    """
    speciality = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=timezone.now)