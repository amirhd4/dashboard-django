import datetime

import pandas
from django.http import HttpResponse
from django.template import loader
from dashboard.models import Products, ProductChanges
import jdatetime

def dashboard(request):
    pds = Products.objects.all().values()
    template = loader.get_template('dashboard.html')
    for i in range(pds.__len__()):
        pds[i]["product_date"] = convert_to_persian_date(pds[i])
    context = {
        "pds": pds
    }
    return HttpResponse(template.render(context, request))

def aboutus(request):
    template = loader.get_template("aboutus.html")
    return HttpResponse(template.render({}, request))

def details(request, pid):
    pds = Products.objects.filter(product_id=pid).values()
    pdcs = ProductChanges.objects.filter(product_id=pid).values().order_by("-product_date")
    if not (not pds and not pdcs):
        pd = pds[0]
        for i in range(pdcs.__len__()):
            pdcs[i]["product_date"] = convert_to_persian_date(pdcs[i])
        pd["product_date"] = convert_to_persian_date(pds[0])
    else:
        pd, pdcs = [], []
    context = {
        "pd": pd,
        "pdcs": pdcs
    }
    template = loader.get_template("details.html")
    return HttpResponse(template.render(context, request))

def convert_to_persian_date(pd):
    return jdatetime.datetime.fromtimestamp(pd["product_date"].timestamp()).__format__('%Y/%m/%d %H:%M:%S')


def export_product_changes_to_excel(request, pid):
    pdcs = ProductChanges.objects.filter(product_id=pid).values()

    for i in range(len(pdcs)):
        dt = datetime.datetime.fromtimestamp(pdcs[i]["product_date"].timestamp())
        pdcs[i]["product_date"] = dt.replace(tzinfo=None)
        pdcs[i]["product_date"] = convert_to_persian_date(pdcs[i])
    df = pandas.DataFrame(list(pdcs))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=pdcs.xlsx'

    df.to_excel(response, index=False, engine='openpyxl')

    return response

def export_products_to_excel(request):
    pds = Products.objects.all().values()

    for i in range(len(pds)):
        dt = datetime.datetime.fromtimestamp(pds[i]["product_date"].timestamp())
        pds[i]["product_date"] = dt.replace(tzinfo=None)
        pds[i]["product_date"] = convert_to_persian_date(pds[i])
    df = pandas.DataFrame(list(pds))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=pdcs.xlsx'

    df.to_excel(response, index=False, engine='openpyxl')

    return response
