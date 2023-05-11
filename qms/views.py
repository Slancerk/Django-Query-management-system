from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , 'new.html')

def about(request):
    return HttpResponse("this is about page")
def service(request):
    return HttpResponse("this is services page")
