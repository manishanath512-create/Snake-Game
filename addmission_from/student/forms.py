from django import forms
from .models import StudentAdmission 

class AdmissionForm(forms.modelFron):
    class meta:
        model=StudentAdmission
        fields='__all__'
