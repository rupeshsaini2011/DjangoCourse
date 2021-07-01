from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import *
from .models import *
from django.forms import ValidationError

class InstituteRegistrationForm(forms.Form):
	username = forms.CharField(max_length=21 , required = True)
	name = forms.CharField(max_length=21 , required = True)    
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
	institue= forms.ModelChoiceField(queryset=Institute.objects.all())
	password = forms.CharField(widget=forms.PasswordInput)

class StudentRegistrationForm(forms.Form):
	username = forms.CharField(max_length=21 ,required = True)
	first_name = forms.CharField(max_length=21,required = True) 
	last_name = forms.CharField(max_length=21,required = True)     
	email = forms.EmailField(max_length=25,required = True)     
	phone_number = forms.IntegerField()    
	course= forms.ModelChoiceField(queryset=Course.objects.all())
	password = forms.CharField(widget=forms.PasswordInput)    


class LoginForm(forms.Form):
	username = forms.CharField(max_length=21,required = True)
	password = forms.CharField(widget=forms.PasswordInput)

"""    
yet to be done! not completed.
REGISTRATION_CHOICES = (
	('Institute', 'Institute'),
	('Teacher', 'Teacher'),
	('Student', 'Student'),
)

class SelectRegistration(forms.Form):
	register_user = forms.ChoiceField(choices=[REGISTRATION_CHOICES],widget=forms.RadioSelect(), required=False)

"""

# if== register_user==institue
	#render return((Reverse institute_register ))