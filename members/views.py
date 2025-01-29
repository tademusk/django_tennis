from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("Hello there")

def first(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
