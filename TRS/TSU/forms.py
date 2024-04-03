from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Nation, Product, Record, Sex, Purpose

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name','last_name','Nationality','Sex','Birth_date','Passport',
                  'Arrival_date','Departure_date','Purpose','Hotel','Id_document']
        
# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'Nationality', 'Sex',
                  'Birth_date','Passport','Arrival_date','Departure_date',
                  'Purpose','Hotel','Id_document']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'Hotel': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_User': forms.TextInput(attrs={'class': 'form-control'}),
        
        }

class NationalityForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = '__all__'
        widgets = {
            'nationality':forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_visiter':forms.TextInput(attrs={'class': 'form-control'}),
        }

class SexForm(forms.ModelForm):
    class Meta:
        model = Sex
        fields = '__all__'
        widgets = {
            'Gender':forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_sex':forms.TextInput(attrs={'class': 'form-control'}),
        }

class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = '__all__'
        widgets = {
            'Kind_visit':forms.TextInput(attrs={'class': 'form-control'}),
            'count':forms.TextInput(attrs={'class': 'form-control'}),
        }
