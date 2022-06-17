from django.http import HttpResponse
from django.shortcuts import render

# def home_page(request):
#     return HttpResponse("<h1>Hello World</h1>")

def home_page(request):
    my_title = "Hello there..."
    return render(request, "hello_world_bs.html", {"title": my_title})

def about_page(request):
    return render(request, "hello_world_bs.html", {"title": "About us"})

def contact_page(request):
    return render(request, "hello_world_bs.html", {"title": "Contact us"})