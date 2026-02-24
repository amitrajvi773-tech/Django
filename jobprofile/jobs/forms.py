from django import forms
from .models import Job
from .models import Application

class JobForm(forms.ModelForm):
       class Meta:
           model = Job
           fields = ['title', 'description', 'company_name', 'location', 'salary']
           
class Applicationform(forms.ModelForm):
    class Meta:
        model=Application
        fields=['cover_letter']