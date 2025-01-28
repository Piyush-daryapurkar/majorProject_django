from django import forms
from .models import Manager_data

state_choice=(
       ("mp","madhyyapradesh"),
    )

class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager_data
        fields=['name','email','password','birth_date','joining_date','emp_id']


class Manager_additional_data(forms.Form):
    image=forms.ImageField()
    pancard=forms.CharField(max_length=12)
    aadharcard=forms.CharField(max_length=12)
    address=forms.CharField(max_length=150)
    state=forms.CharField(choices=state_choice)