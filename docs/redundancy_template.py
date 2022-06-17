from re import template
from tempfile import tempdir
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from matplotlib.style import context

def home_page(request):
    my_title = "Hello there..."
    return render(request, "hello_world_bs.html", {"title": my_title})

def example_page(request):
    context         = {"title": "Example"}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)