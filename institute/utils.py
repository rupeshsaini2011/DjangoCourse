from .models import Institute, Teacher, Student


def getInstitute(user):
	if Institute.objects.filter(user=user).count()>0:
		return Institute.objects.get(user=user)
	else:
		return None

def getTeacher(user):
	if Teacher.objects.filter(user=user).count()>0:
		return Teacher.objects.get(user=user)
	else:
		return None



def getStudent(user):
	if Student.objects.filter(user=user).count()>0:
		return Student.objects.get(user=user)
	else:
		return None