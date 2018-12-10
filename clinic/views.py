from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'clinic/department/department_list.html', {'departments': departments})


@login_required
def department_doctors(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'clinic/doctor/department_doctors.html',  {'department': department},)
