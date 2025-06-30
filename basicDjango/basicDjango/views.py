
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Aliens, We are working with Django!")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("About page: Using Django for fast backend development!")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Contact with Django dev community!!")
    return render(request, 'website/contact.html')

