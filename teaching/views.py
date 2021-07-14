from django.shortcuts import  HttpResponseRedirect, render,  redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView, View, DetailView
from .models import *
from django.contrib.auth import *
from .forms import *
from django.db import transaction 
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate

# ------------------------------------------------index page-------------------------------------------
class IndexTemplateView(TemplateView):
	template_name = "index.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
	  
		context['courses'] = Course.objects.all()     
		context['teachers'] = Teacher.objects.all() 
		context['categories'] = Category.objects.all() 
		context['popular_courses'] = Course.objects.filter(is_popular=True)
		context['testimonial'] = Testimonial.objects.all()  
		context['blogs'] = Blog.objects.all()
			
		return context
		 
 

class IndexTemplateView2(TemplateView):
	template_name = "index2.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
	  
		context['courses'] = Course.objects.all()     
		context['teachers'] = Teacher.objects.all() 
		context['categories'] = Category.objects.all() 
		context['popular_courses'] = Course.objects.filter(is_popular=True)
		context['testimonial'] = Testimonial.objects.all()  
		context['blogs'] = Blog.objects.all()
			
		return context


class CourseTemplateView(ListView):
	template_name = 'courses.html' 
	model = Course
	context_object_name = "courses"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['popular_courses'] = Course.objects.filter(is_popular=True)
		return context
	

	def get_queryset(self):
		qs = Course.objects.all()
		request = self.request
		category_id = request.GET.get('category_id', None)
		if category_id:		
			qs = qs.filter(category__id = category_id)

		return qs
		

class Category_CourseView(DetailView):
	template_name = 'category_course.html' 
	model = Course
	context_object_name = "course"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

	   
		context['categories'] = Category.objects.all()
		
		return context


class CourseDetailView(DetailView):
	template_name = 'coursedetail.html'
	model = Course
	context_object_name = "course"



	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		
		context['categories'] = Category.objects.all()

		
		return context


class TeacherDetailView(DetailView):
	template_name = 'teacherdetail.html'
	model = Teacher
	context_object_name = "teacher"
	


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['course'] = Course.objects.all() 
		return context


class StudentHomeView(DetailView):
	template_name = 'studenthome.html'
	model = Student
	context_object_name = "student"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		return context

class TeacherHomeView(DetailView):
	template_name = 'teacherhome.html'
	model = Teacher
	context_object_name = "teacher"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		return context


class InstituteHomeView(DetailView):
	template_name = 'institutehome.html'
	model = Institute
	context_object_name = "institute"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		return context


#------------------------------------------search results----------------------------------------------	  
class SearchResultView(ListView):
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

		
def registeration(data, reg_type):
	username = data['username']
	phone_number = data['phone_number']
	email = data['email']
	password = data['password']
	first_name = data['first_name']
	last_name = data['last_name']
	with transaction.atomic():
		user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name, last_name=last_name)
		if reg_type=='I':
			name =data['name']
			address = data['address']
			Institute.objects.create(user=user, contact=phone_number, address=address,name=name)
		elif reg_type=='T':
			Teacher.objects.create(user=user, contact=phone_number)
		elif reg_type=='S':
			Student.objects.create(user=user, contact=phone_number)
		
					

class RegistrationView(TemplateView):
	template_name = 'registration.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
# ---------------------------------registration for institutions---------------------------------------  


class InstituteRegisterView(FormView):
	form_class=InstituteRegistrationForm
	template_name='signup_institute.html'
	success_url='/'

	def form_valid(self, form):
		registeration(form.cleaned_data, 'I')
		return super().form_valid(form)

	
# ----------------------------------registration for Teacher------------------------------------------    

class TeacherRegistration(FormView):
	form_class=TeacherRegistrationForm
	template_name= 'signup_teacher.html'
	success_url='/'

	def form_valid(self, form):
		registeration(form.cleaned_data, 'T')
		return super().form_valid(form)


# -------------------------------registration for student --------------------------------

class StudentRegistration(FormView):
	form_class=StudentRegistrationForm
	template_name= 'signup_student.html'
	success_url='/'    

	def form_valid(self, form):
		registeration(form.cleaned_data, 'S')
		return super().form_valid(form)

#ERROR IN course=course
# --------------------------------------------login part----------------------------------------------

class LoginFormView(FormView):
	form_class=LoginForm
	template_name= 'login.html'
	success_url='/login' 



	def form_valid(self, form):
		username=form.cleaned_data['username']
		password= form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		#if Institute.objects.filter(user=user).first():
		if user:
			if user.is_active:
				login(self.request, user)  
				messages.error(self.request, "success", extra_tags='alert alert-success')
				return redirect(reverse_lazy("teaching:index"))
			else:
				# If account is not active:
				messages.error(self.request, 'pls check username and password!',extra_tags='alert alert-danger')
				return render('')

		messages.error(self.request, 'pls check username and password!',extra_tags='alert alert-danger')
		return super().form_valid(form)

class LogoutView(View):
	def get(self, request):
		logout(request)
		return redirect(reverse_lazy("teaching:index"))
		
