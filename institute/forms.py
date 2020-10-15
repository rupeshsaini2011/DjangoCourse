from django import forms
from django.contrib.auth import get_user_model 
from .models import Institute

User=get_user_model()

class guest_form(forms.Form):
    email=forms.EmailField()
class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class Registerform(forms.Form):
    name=forms.CharField()
    username = forms.CharField()
    email= forms.EmailField()
    phone =forms.CharField()
    address=forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs= User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean(self):
        # data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("passwords must match")
        # return data

class Studentform(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    phone=forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    
    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs= User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean(self):
        # data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("passwords must match")
        # return data

class Teacherform(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    institute=forms.ModelChoiceField(queryset=Institute.objects.all())
    # institute=forms.ModelChoiceFiel/d(Registerform)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    
    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs= User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean(self):
        # data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("passwords must match")
        # return data