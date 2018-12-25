from django import template
from django.utils import timezone
from datetime import timedelta, datetime, tzinfo
from clinic.models import Doctor, Appointment

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


@register.inclusion_tag('clinic/appointment/appointment_list.html')
def show_doctor_today_appointment(_object):
    _pk = _object.pk
    print(_pk)
    start_date = datetime.now(timezone.get_current_timezone()).date() - timedelta(days=1)
    end_date = datetime.now(timezone.get_current_timezone()).date() + timedelta(days=1)
    appointments = Appointment.objects.filter(
        doctor__exact=_pk,
        startDateTime__range=(start_date, end_date)
    ).order_by('startDateTime')
    return {'appointments': appointments}
