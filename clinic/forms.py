from django import forms
from django.forms import DateTimeInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy
import datetime
import pytz

from .models import Appointment, Doctor, UserProfile, Service, AppointmentStatus


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {'startDateTime': ugettext_lazy('Start time'), 'endDateTime': ugettext_lazy('End Time'), 'user': ugettext_lazy('Patient')}

        widgets = {
            'startDateTime': DateTimeInput(attrs={'data': 'DateTimePicker', 'id': 'start_date_picker'}),
            'endDateTime': DateTimeInput(attrs={'data': 'DateTimePicker', 'id': 'end_date_picker'}),
        }

        # def clean(self):
        #     cleaned_data = super().clean()
        #     start_date = cleaned_data.get('startDateTime')
        #     end_date = cleaned_data.get('endDateTime')
        #
        #     if end_date <= start_date:
        #         msg = 'End Date should be greater than Start Date'
        #         self.add_error('endDateTime', msg)
