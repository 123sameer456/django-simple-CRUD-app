from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id' , 'Student_Name' , 'Father_Name' , 'Contact_Number',
                  'Address' , 'Course' , 'Timing' , 'Days']
        widgets = {
            '' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Student_Name' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Father_Name' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Contact_Number' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Address' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Course' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Days' : forms.TextInput(attrs={'class': 'form-control'}) , 
            'Timing' : forms.TextInput(attrs={'class': 'form-control'}) , 
        }