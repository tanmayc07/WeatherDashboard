from django import forms
from dashboard.models import CityModel


class CityForm(forms.ModelForm):

    class Meta:
        model = CityModel
        fields = ('city_name',)
        widgets = {
            'city_name': forms.TextInput(attrs={'class': 'form-control my-3 p-3', 'placeholder': 'City Name...'})
        }
