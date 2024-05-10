from django import forms

from airportoffice.models import Airports

class Airportform(forms.ModelForm):
    class Meta:  
        model = Airports  
        fields = "__all__"
        