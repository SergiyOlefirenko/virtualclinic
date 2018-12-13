from django.conf.urls import url
from clinic import views as clinic_views


urlpatterns = [
    url(r'patient/(?P<pk>\d+)/appointments/$', clinic_views.patient_appointment_list, name='patient_appointment_list'),
    url(r'departments/$', clinic_views.patient_department_list, name='patient_department_list'),
]
