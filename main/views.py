from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def snews(request):
    return render(request,'single.html')

def category(request):
    return render (request, 'category.html')