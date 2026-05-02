from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method =='POST':
        form = Registration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email = form.cleaned_data['email']
            return HttpResponse('/student/register/')

    else:
        form = Registration()
        return render(request,'student/register.html',{'form':form})