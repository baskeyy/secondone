from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def iron(request):
    return HttpResponse('iron man')
def man(request):
    return HttpResponse('avengers age of ultron')

