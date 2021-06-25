from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Institute(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=127)
    contact = models.SmallIntegerField()    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_institute')   

    def __str__(self):
        return str(self.user)   

class Teacher(models.Model):   
    institution = models.ForeignKey(Institute,on_delete=models.CASCADE, related_name="teachers") 
    contact = models.SmallIntegerField()    
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_teacher")
    about = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user) 

class Currency(models.Model):
    name = models.CharField(max_length=11)     

    def __str__(self):
        return self.name 

class Category(models.Model):
    category = models.CharField(max_length=127)

    def __str__(self):
        return self.category 
    

class Course(models.Model):
    name = models.CharField(max_length=127)
    institution= models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='institutes')
    main_teacher= models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name="teacher_courses") 
    price= models.DecimalField(max_digits=11, decimal_places=2)
    currency= models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_courses")
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_courses" , null = True, blank= True)
    is_popular = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name 

 

class Subject(models.Model):
    name = models.CharField(max_length=127)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_subjects')  

    def __str__(self):
        return self.name 

class Schedule(models.Model):
    DAYS=(("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"),("Friday","Friday"),("Saturday","Saturday"),("Sunday","Sunday")) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_schedules')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_schedules')
    year = models.CharField(max_length=11)
    day = models.CharField(max_length=12,choices=DAYS)
    time_from = models.TimeField()
    time_to=models.TimeField() 
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_schedules')

    def __str__(self):
        return self.subject.name

class Period(models.Model):
    schedule= models.ForeignKey(Schedule, on_delete=models.CASCADE,related_name='schedule_periods')
    date= models.DateField()
    assignment = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name 

class Student(models.Model): 
    contact = models.SmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_student")

    def __str__(self):
        return self.name 

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_enrollments')
    order_id = models.CharField(max_length=127)
    payment_id = models.CharField(max_length=127)
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    currency= models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_enrollments")

    def __str__(self):
        return self.order_id 
    

class Testimonial(models.Model):
    review = models.TextField(blank=True,null=True)
    name = models.CharField(max_length=127)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_testimonial")

    def __str__(self):
        return self.name

