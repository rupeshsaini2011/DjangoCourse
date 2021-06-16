from .models import Institute, Teacher, Student

def getInstitute(user):
    return Institute.objects.filter(user=user).first()
    
def getTeacher(user):
    return Teacher.objects.filter(user=user).first()

def getStudent(user):
    return Student.objects.filter(user=user).first()
