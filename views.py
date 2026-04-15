from django.shortcuts import render
from student.forms import Registration, Login

def registration(req):
    fm = Registration()
    # Pass the form instance to your template via a context dictionary
    return render(req, 'student/registration.html', {'form': fm})


def login(req):
    fm = Login()
    return render(req, 'student/login.html', {'form': fm})
