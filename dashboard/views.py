from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from dashboard.models import Products


def dashboard(request):
    pds = Products.objects.all().values()
    template = loader.get_template('dashboard.html')
    context = {
        "pds": pds
    }
    return HttpResponse(template.render(context, request))

def aboutus(request):
    template = loader.get_template("aboutus.html")
    return HttpResponse(template.render({}, request))