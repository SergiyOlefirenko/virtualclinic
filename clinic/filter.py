from accounts.models import UserProfile
import django_filters


class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', ]
