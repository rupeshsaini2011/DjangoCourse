from django.urls import path
from .views import *
from .import views

app_name='teaching'


urlpatterns = [   
path('', IndexTemplateView.as_view(), name='index'),
path('index2/', IndexTemplateView2.as_view(), name='index2'), 
path('courses/',  CourseView.as_view(), name='courses'),
path('categorycourse/<int:pk>',  Category_CourseView.as_view(), name='category_course'),
path('coursedetail/<int:pk>/', CourseDetailView.as_view(), name='coursedetail'),
path('registration/', RegistrationView.as_view(), name='registration'),
path('teacherdetail/<int:pk>/', TeacherDetailView.as_view(), name='teacherdetail'),
path('studenthome/<int:pk>/', StudentHomeView.as_view(), name='studenthome'),
path('teacherhome/<int:pk>/', TeacherHomeView.as_view(), name='teacherhome'),
path('institutehome/<int:pk>/', InstituteHomeView.as_view(), name='institutehome'),
# path('searchresults/',views.SearchResultsView.as_view(), name='search-results'),
path('teachers/', views.TeacherView.as_view(), name='teachers'),
path('blogs/',  BlogView.as_view(), name='blogs'),
path('blogdetail/<int:pk>/', BlogDetailView.as_view(), name='blogdetail'),
# path('course/', views.CoursesListView.as_view(), name='course'),
path('institutes/', views.InstituteView.as_view(), name='institutes'),
path('registerinstitute/', views.InstituteRegisterView.as_view(), name='register_institute'),
path('registerteacher/', views.TeacherRegistration.as_view(), name='register_teacher'),
path('registerstudent/', views.StudentRegistration.as_view(), name='register_student'),
path('login/', views.LoginFormView.as_view(), name='login'),
path('logout/', views.LogoutView.as_view(),name='logout'),
path('payment-status/<str:oid>/', PaymentStatusView.as_view(), name='payment-status'),
path('payment/<int:cid>/', PaymentView.as_view(), name='payment'), 

]