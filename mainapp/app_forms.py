from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mainapp.models import Product, CustomUser


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    phone = forms.CharField(max_length=20)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'dob', 'phone', 'password1', 'password2']


class UpdateUser(forms.ModelForm):
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    # email = forms.EmailField(max_length=40)
    # phone_number = forms.CharField(max_length=20)
    # dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['phone_number', 'dob', 'profile_picture']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }
