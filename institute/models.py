from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Institute(models.Model):
  user= models.OneToOneField(User, on_delete= models.CASCADE)
  phone=models.CharField(max_length=15)
  address=models.CharField(max_length=100)
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name
    
class Teacher(models.Model):
  institute=models.ForeignKey(Institute, on_delete=models.CASCADE, related_name="teachers")
  phone=models.CharField(max_length=10)
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  salary=models.DecimalField(max_digits=8, decimal_places=2)
  qualification=models.CharField(max_length=100)
  staff=models.CharField(max_length=50)
  
  @property
  def full_name(self):
    return self.user.first_name+ " " + self.user.last_name

  def __str__(self):
    return self.full_name

class InstituteClass(models.Model):
  name=models.CharField(max_length=10)
  section=models.CharField(max_length=10, blank=True, null=True)
  class_teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_classes")
  def __str__(self):
    return self.name

class Subject(models.Model):
  teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_subject")
  subject=models.CharField(max_length=50)
  classappointed=models.ForeignKey(InstituteClass, on_delete=models.CASCADE)

  def __str__(self):
    return self.subject
  
class Schedule(models.Model):
  days=(("Monday","Monday"), 
  ("Tuesday","Tuesday"), ("Wednesday", "Wednesday"),
   ("Thursday", "Thursday"), 
  ("Friday", "Friday"), ("Saturday","Saturday"),
   ("Sunday", "Sunday"))

  subject=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_schdule")
  day=models.CharField(max_length=50, choices=days)
  time_from=models.TimeField()
  time_to=models.TimeField()
  year=models.IntegerField(default=2020)
  is_active=models.BooleanField(default=True)

 
  
class Period(models.Model):

  schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="periods")
  timstamp=models.DateField()
 

class Student (models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE, related_name= "user_student")
  phone=models.CharField(max_length=50)
  classes=models.ManyToManyField(InstituteClass, related_name="class_students")
  institute=models.ForeignKey(Institute, on_delete=models.SET_NULL, null=True, blank=True, related_name= "institute_students")
  







