
from django.urls import path
from django.contrib.auth.views import LogoutView
from institute.views import InstituteView, Login, instituteregister, studentregister, teacherregister,  schedule, studentinfo, studentlist, teacherinfo, insititutelist, institute, subjectlist, subjectsinfo
app_name="institute"

urlpatterns = [
    path("login/", Login, name="Login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", instituteregister, name="register"),
    path("teacherregister/", teacherregister, name="teacherregister"),
    path("studentregister/", studentregister, name="studentregister"),
    path("teacherinfo/<int:tid>", teacherinfo, name="teacherinfo"),
    path("institute/<int:iid>", institute, name="institute"),
    path("institutelist/", insititutelist, name="institutelist"),
    path("subjectlist", subjectlist, name="subjectlist"),
    path("subjectsinfo/<int:sid>", subjectsinfo, name="subjectsinfo"),
    path("studentlist", studentlist, name="studentlist"),
    path("students<int:sid>", studentinfo, name="studentinfo"),
    path("schedule/<int:sid>", schedule, name="schedule"),

    path('institute_detail/<int:pk>/',  InstituteView.as_view() , name='institute_detail_view'),
    
]

