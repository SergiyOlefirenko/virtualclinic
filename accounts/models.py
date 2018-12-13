from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    MARITAL_STATUS_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_regex = RegexValidator(
        regex=r'^\+\d{8,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    birth_date = models.DateTimeField('birth_date')
    address = models.CharField(max_length=250)
    note = models.TextField(max_length=4000)
    photo = models.CharField(max_length=250, default='img/patients/def_patient.jpeg')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
