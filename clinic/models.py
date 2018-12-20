from django.db import models
from django.core.validators import RegexValidator
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse


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
    description = models.TextField(max_length=400)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.department


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=450)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True, related_name='doctors')

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
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='patient_appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    status = models.ForeignKey(AppointmentStatus, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('patient_appointment_list', kwargs={'pk': self.user.user.pk})


class FeedbackRate(models.Model):
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.rate


class PatientFeedback(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    rate = models.ForeignKey(FeedbackRate, on_delete=models.SET_NULL, blank=True, null=True)
    feedback = models.TextField(max_length=4000)


class Chat(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    inclusion_date = models.DateTimeField()
    message = models.CharField(max_length=250)
    chat = models.OneToOneField(Chat, on_delete=models.CASCADE)


class FamilyDoctor(models.Model):
    patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, unique=False)
