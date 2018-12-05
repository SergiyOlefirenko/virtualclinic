from django.shortcuts import render
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
    return render(request, 'doctor/doctor_home.html')
