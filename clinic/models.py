from django.db import models
from django.core.validators import RegexValidator
from accounts.models import UserProfile


# Create your models here.
class ClinicContactInfo(models.Model):
    clinic_name = models.CharField(max_length=250)
    clinic_address = models.CharField(max_length=250)
    phone_regex = RegexValidator(
        regex=r'^\+\d{8,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    clinic_phone_number = models.CharField(validators=[phone_regex], max_length=16)
    clinic_email = models.CharField(max_length=250)

    def __str__(self):
        return self.clinic_name


class AboutInfo(models.Model):
    aboutInfo = models.TextField(max_length=4000)


class Department(models.Model):
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.department


class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class AppointmentStatus(models.Model):
    statusTitle = models.CharField(max_length=50)

    def __str__(self):
        return self.statusTitle


class Service(models.Model):
    serviceName = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.serviceName


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    status = models.ForeignKey(AppointmentStatus, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.startDateTime + ' ' + self.endDateTime


class FeedbackRate(models.Model):
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.rate


class PatientFeedback(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    rate = models.ForeignKey(FeedbackRate, on_delete=models.SET_NULL, blank=True, null=True)
    feedback = models.TextField(max_length=4000)


class PatientDoctorMessage(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.CharField(max_length=250)