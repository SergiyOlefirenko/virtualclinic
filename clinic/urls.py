from django.conf.urls import url
from clinic import views as clinic_views


urlpatterns = [
    url(r'patient/(?P<pk>\d+)/appointments/$', clinic_views.patient_appointment_list, name='patient_appointment_list'),
    url(r'departments/$', clinic_views.patient_department_list, name='patient_department_list'),
    url(r'appointment/new/$', clinic_views.NewAppointmentView.as_view(), name='new_appointment'),
    url(r'appointment/(?P<pk>\d+)/$', clinic_views.AppointmentDetailsView.as_view(), name='appointment_details'),
    url(r'appointment/(?P<pk>\d+)/edit/$', clinic_views.EditAppointmentView.as_view(), name='appointment_edit'),
    url(r'appointment/(?P<pk>\d+)/delete/$', clinic_views.DeleteAppointmentView.as_view(), name='appointment_delete'),
    url(r'patient/family_doctor/new', clinic_views.FamilyDoctorCreate.as_view(), name='family_doctor_create'),
    # doctor urls
    url(r'^doctor/$', clinic_views.doctor_home, name='doctor_home'),
    url(r'^departments/(?P<pk>\d+)/doctors/$', clinic_views.department_doctors, name='department_doctors'),
    url(r'doctor/(?P<pk>\d+)/$', clinic_views.DoctorDetails.as_view(), name='doctor_details'),
]
