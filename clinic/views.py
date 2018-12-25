from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from clinic.forms import AppointmentForm, ManageFamilyDoctorForm
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
    return render(request, 'clinic/doctor/department_doctors.html', {'department': department}, )


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
    appointments = user.patient.patient_appointments.order_by('-startDateTime')
    return render(request, 'clinic/patient/patient_appointment_list.html', {'appointments': appointments})


@method_decorator(login_required, name='dispatch')
class NewAppointmentView(CreateView):
    model = Appointment
    # fields = '__all__'
    form_class = AppointmentForm
    template_name = 'clinic/appointment/new_appointment.html'


@method_decorator(login_required, name='dispatch')
class AppointmentDetailsView(DetailView):
    model = Appointment
    template_name = 'clinic/appointment/appointment_details.html'


@method_decorator(login_required, name='dispatch')
class EditAppointmentView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'clinic/appointment/update_appointment.html'


@method_decorator(login_required, name='dispatch')
class DeleteAppointmentView(DeleteView):
    template_name = 'clinic/appointment/delete_appointment.html'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Appointment, pk=pk_)

    def get_success_url(self):
        patient_pk_ = self.request.user.pk
        return reverse('patient_appointment_list', args=[patient_pk_])


@method_decorator(login_required, name='dispatch')
class FamilyDoctorCreate(CreateView):
    model = FamilyDoctor
    form_class = ManageFamilyDoctorForm
    template_name = 'clinic/patient/patient_add_family_doctor.html'

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


@method_decorator(login_required, name='dispatch')
class DoctorDetails(DetailView):
    model = Doctor
    template_name = 'clinic/doctor/doctor_details.html'
