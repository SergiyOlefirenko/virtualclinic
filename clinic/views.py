from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .filter import PatientFilter
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts_info(request):
    contacts = ClinicContactInfo.objects.all()
    return render(request, 'contacts/contacts_info.html', {'contacts': contacts})


@login_required
def doctor_home(request):
    return render(request, 'clinic/doctor/doctor_home.html')


@login_required
def patient_department_list(request):
    departments = Department.objects.all()
    return render(request, 'clinic/patient/patient_department_list.html', {'departments': departments})


@login_required
def department_doctors(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'clinic/doctor/department_doctors.html',  {'department': department},)


@login_required
def patient_search(request):
    patients = UserProfile.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=patients)
    return render(request, 'includes/patient_search_form.html', {'filter': patient_filter})


@login_required
def reception_home(request):
    return render(request, 'clinic/reception/reception_home.html')


@login_required
def patient_appointment_list(request, pk):
    user = get_object_or_404(User, pk=pk)
    appointments = user.patient.patient_appointments.all()
    return render(request, 'clinic/patient/patient_appointment_list.html', {'appointments': appointments})
