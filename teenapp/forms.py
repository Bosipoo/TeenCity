from django import forms
from django.forms import ModelForm
from .models import Teen

BA_CHOICES = [('Y','Yes'),('N','No')]
GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
LEVEL_CHOICES = [
    ('Junior secondary school', 'Junior secondary school'),
    ('Senior secondary school', 'Senior secondary school'),
    ('Getting ready for university', 'Getting ready for university'),
    ('In university','In university'),
    ('Working', 'Working'),
    ('Other', 'Other')
]

class Teens(forms.ModelForm):
    bornagain = forms.ChoiceField(choices=BA_CHOICES, widget=forms.RadioSelect())
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Teen
        fields = ['firstname','lastname','othername','email','gender','dob','age',
                    'phone','school','level','cclass','address','ambition','bornagain','hobbies']
        