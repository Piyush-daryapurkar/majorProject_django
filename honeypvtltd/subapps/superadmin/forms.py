from django import forms
from .models import Manager_data

class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager_data
        fields=['name','email','password','birth_date','joining_date','emp_id']