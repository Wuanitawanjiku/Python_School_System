from django.shortcuts import render

# Create your views here.
#Views handle http requests

from django.shortcuts import render
from .forms import StudentRegistrationForm

def register_student(request):
    form = StudentRegistrationForm()            #creating an instance of a class because we want to render it
    return render(request, "register_student.htm", {"form":form})

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = StudentRegistrationForm()
        return render(request, "register_student.htm", {"form":form})

