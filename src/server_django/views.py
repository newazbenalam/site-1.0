from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from matplotlib.pyplot import title

# def home_page(request):
#     return HttpResponse("<h1>Hello World</h1>")

def home_page(request):
    my_title = "Hello there..."
    return render(request, "hello_world_bs.html", {"title": my_title})

def home_page1(request):
    my_title = "Hello there..."
    context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]} 
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    return render(request, "hello_world_bs.html", {"title": "Contact us"})

def example_page(request):
    context         = {"title": "Example"}
    template_name   = "hello_world_bs.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)