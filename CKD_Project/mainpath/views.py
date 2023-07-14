from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def say_hello(request):
    return HttpResponse('hello world')

def render_form(request):
    return render(request, "form.html")

def patient_form(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
    else:
        form= UserCreationForm()
    return render(request,'form.html',{'form':form})