from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def student_show(request):
    student = Student.objects.order_by('roll_no')
    return HttpResponse(request, 'student/student_show.html', {'student':student})
