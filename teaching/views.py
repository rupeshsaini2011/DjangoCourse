from django.shortcuts import *
from django.views.generic import *
from .models import *
from django.contrib.auth import *
from .forms import *
from django.db import transaction 
from django.urls import *
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate

# ------------------------------------------------index page-------------------------------------------
class IndexTemplateView(TemplateView):
    template_name = "index.html"
#---------------------------------------------searching algo-------------------------------------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.all()        
        context['course'] = course        
        return context
  
#------------------------------------------search results----------------------------------------------
class SearchResultsView(ListView):
    model= Course #course
    template_name='search_results.html'  

    def post(self, request, *args, **kwargs):
        course = request.POST.get('course', "")
        sechedule= Schedule.objects.all()        
        if course:
            sechedule= sechedule.filter(subject__course=course)
        return render(self.request, self.template_name, context={'sechedule': sechedule})    
#------------------------------------------------------------------------------------------------------

class TeacherListView(ListView):
    model = Teacher
    template_name='teacher_list.html'

class CoursesListView(ListView):
    model = Course
    template_name = 'course_list.html'		

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'

reg_type = ('I','T','S')

def registeration(data, reg_type):
    username = data['username']
    phone_number=data['phone_number']
    name =data['name']
    email = data['email']
    address = data['address']
    password = data['password']
    first_name =data['first_name']
    last_name = data['last_name']
    about = data['about']
    institue= data['institue']
    course = data['course']
    with transaction.atomic():
        user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name, last_name=last_name)
        if reg_type=='I':
                Institute.objects.create(user=user, contact=phone_number, address=address,name=name)
        elif reg_type=='T':
                Teacher.objects.create(user=user, contact=phone_number,about=about,institue=institue)
        elif reg_type=='S':
                Student.objects.create(user=user, contact=phone_number, about=about, course=course)
            
            
            
            
            
        
                    

                    
         
# ---------------------------------registration for institutions---------------------------------------  
class InstituteRegisterView(FormView):
    form_class=InstituteRegistrationForm
    template_name='signup_institute.html'
    success_url='/'

    def form_valid(self, form):
        registeration(InstituteRegistrationForm, 'I')
        return super().form_valid(form)

    
# ----------------------------------registration for Teacher------------------------------------------    
# in template use hidden field reg_type
#('T', 'S', 'I')
#<input type="hidden" value='T">

class TeacherRegistration(FormView):
    form_class=TeacherRegistrationForm
    template_name= 'signup_teacher.html'
    success_url='/'

    def form_valid(self, form):
        registeration(InstituteRegistrationForm, 'T')
        return super().form_valid(form)


# -------------------------------registration for student --------------------------------

class StudentRegistration(FormView):
    form_class=StudentRegistrationForm
    template_name= 'signup_student.html'
    success_url='/'    

    def form_valid(self, form):
        registeration(InstituteRegistrationForm, 'S')
        return super().form_valid(form)

#ERROR IN course=course
# --------------------------------------------login part----------------------------------------------


class LoginFormView(FormView):
    form_class=LoginForm
    template_name= 'login.html'
    success_url='/login' 
# lms dashbord
    def form_valid(self, form):
        username=form.cleaned_data['username']
        password= form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        #if Institute.objects.filter(user=user).first():
        if user:
            if user.is_active:
                login(self.request, user)  
                messages.error(self.request, "success", extra_tags='alert alert-success')
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                messages.error(self.request, 'pls check username and password!',extra_tags='alert alert-danger')
                return render()

        messages.error(self.request, 'pls check username and password!',extra_tags='alert alert-danger')
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
        
