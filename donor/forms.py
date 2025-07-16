from django import forms
from django.contrib.auth.models import User
from . import models
import re

class DonorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

class DonorForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields=['bloodgroup','address','mobile','profile_pic']

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.fullmatch(r'\d{10}', str(mobile)):
            raise forms.ValidationError("Enter a valid 10-digit mobile number.")
        return mobile

class DonationForm(forms.ModelForm):
    class Meta:
        model=models.BloodDonate
        fields=['age','bloodgroup','disease','unit']
