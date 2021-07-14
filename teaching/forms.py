from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import *
from .models import *
from django.forms import ValidationError

class InstituteRegistrationForm(forms.Form):
	username = forms.CharField(max_length=21 , required = True)
	first_name = forms.CharField(max_length=21,required = True)   
	last_name = forms.CharField(max_length=21,required = True)    
	email = forms.EmailField(max_length=25 , required = True)
	address= forms.CharField(max_length=127, required = True)  
	phone_number = forms.IntegerField()    
	password = forms.CharField(widget=forms.PasswordInput)    


class TeacherRegistrationForm(forms.Form):
	username = forms.CharField(max_length=21 ,required = True)
	first_name = forms.CharField(max_length=21,required = True)   
	last_name = forms.CharField(max_length=21,required = True) 
	email = forms.EmailField(max_length=25,required = True)
	address= forms.CharField(max_length=127,required = True)  
	phone_number = forms.IntegerField()
	about = forms.CharField(max_length=121,required = True)
	password = forms.CharField(widget=forms.PasswordInput)


class StudentRegistrationForm(forms.Form):
	username = forms.CharField(max_length=21 ,required = True)
	first_name = forms.CharField(max_length=21,required = True) 
	last_name = forms.CharField(max_length=21,required = True)     
	email = forms.EmailField(max_length=25,required = True)     
	phone_number = forms.IntegerField()    
	password = forms.CharField(widget=forms.PasswordInput)    


class LoginForm(forms.Form):
	username = forms.CharField(max_length=21,required = True)
	password = forms.CharField(widget=forms.PasswordInput)

