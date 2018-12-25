from django import template
from django.utils import timezone
from clinic.models import Doctor

register = template.Library()


@register.inclusion_tag('clinic/appointment/family_doctor_appointment_list_partial.html')
def show_family_doctor_appointments(patient):
        doctor = patient.familydoctor.doctor
        appointments = doctor.doctor_appointments.filter(
            status__id__in=[1, 2],
            startDateTime__gte=timezone.now()
        ).order_by('startDateTime')
        return {'appointments': appointments}


@register.inclusion_tag('clinic/patient/patient_family_doctor_list.html')
def show_doctors_by_department():
    doctors = Doctor.objects.filter(is_family_doctor=True)
    return {'doctors': doctors}
