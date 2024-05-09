from django import forms
from login.models import Register
from django.forms import fields
class Registerform(forms.ModelForm):
    class Meta:  
        model = Register  
        fields = "__all__"
