from django.shortcuts import render
from datetime import datetime

# Create your views here.

# example 1
# def learn_django(req):
#     return render(req, 'course/django.html', context={'name':'Django'})
#
# # example 2
#
# def learn_django(req):
#     name = 'django'
#     duration = '4 month'
#     seats = 10
#     course_details = {'nm': name, 'du':duration, 'st':seats}
#     return render(req, 'course/django.html', course_details)

# ex 3 filter
# def learn_django(req):
#     return render(req, 'course/django.html', context={'name':'Django','desc':'django is the best'})

def learn_django(req):
    d = datetime.now()

    return render(req, 'course/django.html', context={'dt':d})
