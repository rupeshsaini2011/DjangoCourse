from django.urls import *
from .views import *
from .import views

app_name='teaching'


urlpatterns = [   
path('', IndexTemplateView.as_view(), name='index'), 
# path('searchresults/',views.SearchResultsView.as_view(), name='search-results'),
# path('teacher/', views.TeacherListView.as_view(), name='teacher'),
# path('course/', views.CoursesListView.as_view(), name='course'),
# path('subject/', views.SubjectListView.as_view(), name='subject'),
# path('registerinstitute/', views.InstituteRegisterView.as_view(), name='register_institute'),
# path('registerteacher/', views.TeacherRegistration.as_view(), name='register_teacher'),
# path('registerstudent/', views.StudentRegistration.as_view(), name='register_teacher'),
# path('login/', views.LoginFormView.as_view(), name='login'),
# path('logout/', views.LogoutView.as_view(),name='logout'),
]