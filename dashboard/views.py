from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render({}, request))