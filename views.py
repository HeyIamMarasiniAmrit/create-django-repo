# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def home(request):
#     return HttpResponse('Home page')

# def learn_django(request):
#     return HttpResponse('Hello Djano')


# def learn_python(request):
#     return HttpResponse('<h1>Hello python</h1>')

# def learn_php(request):
#     lang = '<h2>hello world</h2>'
#     return HttpResponse(lang)


def home(request):
    return HttpResponse('Home Page')


def myapp1(request):
    return HttpResponse('my app 1')


