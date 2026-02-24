from django.urls import path, include
from course.views import learn_django, learn_python

urlpatterns = [

    path('dj/', learn_django, name='django'),
    path('py/', learn_python, name='python'),
]