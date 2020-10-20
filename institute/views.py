from django.shortcuts import render, HttpResponse, redirect
from .models import  Schedule, Period, Institute, Subject, Student, Teacher
from .forms import Loginform, Registerform, guest_form , Teacherform, Studentform
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LogoutView
from schema.models import Tenant, TenantUser
from django.db import connection, transaction
from django.conf import settings

from django.core.management import call_command
# Create your views here.



# def home(request):
#   return HttpResponse ("this is the home page of our LMS")

def Login(request):
	
    form = Loginform(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('Got a user ' + user.username)
            login(request, user)
            context[form] = Loginform()
            return HttpResponse("hello")
        else:
            return render(request, "institutes/login.html", context)
  
    return render(request, "institutes/login.html", context)



User = get_user_model()

def instituteregister(request):
    form = Registerform(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        phone=form.cleaned_data.get("phone")
        address=form.cleaned_data.get("address")
        name=form.cleaned_data.get("name")
        password =form.cleaned_data.get("password")
        divi_user=settings.DATABASES["default"]["USER"]
        schema=name.split(" ")
        schema= schema[0].lower()    
        # print(institute)
        # print(newuser)
        # print(form.cleaned_data)
        with transaction.atomic():
          with connection.cursor() as cursor:
             tenant=Tenant.objects.create(name = schema)
             tenantuser=TenantUser.objects.create(username=username, tenant=tenant)
             main_user = User.objects.first()
             cursor.execute(f"create schema {schema}")
             cursor.execute(f"grant all privileges on schema {schema} to {divi_user};")  
             cursor.execute(f"set search_path to {schema}")
             call_command("migrate")
             main_user.pk = None
             main_user.save()
             newuser = User.objects.create_superuser(username, email, password)
             institute=Institute.objects.create(user=newuser, phone=phone, address=address, name=name)
             

        # print(institute)
        # print(newuser)
        # print(form.cleaned_data)

    return render(request, "institutes/instituteregister.html", context)

def studentregister(request):
    form = Studentform(request.POST or None)
    context = {
        "form": form
    }
    print(form)
    if form.is_valid():
        username = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        phone=form.clean_data.get("phone")
        password = form.cleaned_data.get("password")
        newuser = User.objects.create_user(username, email, phone, password)
        print(newuser)
        print(form.cleaned_data)
    return render(request, "institutes/studentregister.html", context)


def teacherregister(request):
    form = Teacherform(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        # institute=form.cleaned_data.get("institute")
        password = form.cleaned_data.get("password")
        newuser = User.objects.create_user(username, email, password)
        

        print(newuser)
        print(form.cleaned_data)
    return render(request, "institutes/teacherregister.html", context)


###############################################################################
def studentlist(request):
  return HttpResponse("studentlist")

def institute(request, iid):
  
  context={
    "teachers":Teacher.objects.filter(), 
    'institute': Institute.objects.get(pk=iid)

  }
  return render(request, "institutes/institute.html", context)

def insititutelist(request):
  context={
    "institutes":Institute.objects.all()

  }
  return render(request, "institutes/institutes.html", context)


###############################################
def subjectlist(request):

  context={
    "subjects": Subject.objects.all(),
    "schedules":Schedule.objects.all()
  }

  return render(request, "institutes/subjectlist.html", context)



def subjectsinfo(request, sid):
  context={
    "subjects": Subject.objects.get(pk=sid)
  }
  return render(request, "institutes/subjects.html", context)


################################################################################

def studentlist(request):
  
  context={
    "students": Student.objects.all()
  }
  return render(request, "institutes/studentlist.html", context )
def studentinfo(request, sid):

  context={
    "students": Student.objects.get(pk=sid)
  }
  return render(request, "institutes/students.html", context )
#################################################


def schedule(request, sid):
  context={
    "schedule": Schedule.objects.get(pk=sid),
    "period": Period.objects.get(pk=sid)
  }
  return render(request, "institutes/schedule.html", context)


def instituteinfo(request):
  return HttpResponse("instituetinfo")

def teacherinfo(request, tid):
  return HttpResponse("teacherinfo kaun sae teacher " + str(tid) )

  