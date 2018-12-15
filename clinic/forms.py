from django import forms
from django.forms import DateTimeInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy
import datetime

from .models import Appointment, Doctor, UserProfile, Service, AppointmentStatus


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            'startDateTime': DateTimeInput(attrs={'data': 'DateTimePicker', 'id': 'start_date_picker'}, format="%d %b %Y %H:%M:%S %Z"),
            'endDateTime': DateTimeInput(attrs={'data': 'DateTimePicker', 'id': 'end_date_picker'}, format="%d %b %Y %H:%M:%S %Z"),
        }
