from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts_info(request):
    contacts = ClinicContactInfo.objects.all()
    return render(request, 'contacts/contacts_info.html', {'contacts': contacts})
