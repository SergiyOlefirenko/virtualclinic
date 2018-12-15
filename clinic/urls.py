from django.conf.urls import url
from clinic import views as clinic_views


urlpatterns = [
    url(r'patient/(?P<pk>\d+)/appointments/$', clinic_views.patient_appointment_list, name='patient_appointment_list'),
    url(r'departments/$', clinic_views.patient_department_list, name='patient_department_list'),
    url(r'appointment/new/$', clinic_views.NewAppointmentView.as_view(), name='new_appointment'),
    url(r'appointment/(?P<pk>\d+)/$', clinic_views.AppointmentDetailsView.as_view(), name='appointment_details'),
    url(r'appointment/(?P<pk>\d+)/edit/$', clinic_views.AppointmentEditView.as_view(), name='appointment_edit'),
    url(r'appointment/(?P<pk>\d+)/delete/$', clinic_views.AppointmentDeleteView.as_view(), name='appointment_delete'),
]
