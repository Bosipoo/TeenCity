import django_filters
from dobwidget import DateOfBirthWidget

from .models import *

class TeenFilter(django_filters.FilterSet):
    class Meta:
        model = Teen 
        fields = ['firstname','lastname','dob']
        widgets = {
            'dob': DateOfBirthWidget(),
        }