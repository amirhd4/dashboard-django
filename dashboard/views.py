import datetime

import pandas
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from dashboard.models import Products, ProductChanges
from abc import ABC, abstractmethod
from django.views import View


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

def details(request, pid):
    pds = Products.objects.filter(product_id=pid).values()
    pdcs = ProductChanges.objects.filter(product_id=pid).values().order_by("-product_date")
    if not (not pds and not pdcs):
        pd = pds[0]
    else:
        pd, pdcs = [], []
    context = {
        "pd": pd,
        "pdcs": pdcs
    }
    template = loader.get_template("details.html")
    return HttpResponse(template.render(context, request))


def submit_price(request, pid):
    Products.objects.filter(product_id=pid).update(product_price=request.POST["price"])
    ProductChanges(product_id=pid, product_price=request.POST["price"], product_date=datetime.datetime.now()).save()
    return HttpResponseRedirect(f'/details/{pid}')


class ExportExcel(ABC):
    @abstractmethod
    def get_records(self, pid = None):
        pass

    @staticmethod
    def create_excel_file(pdcs, req):
        for i in range(len(pdcs)):
            dt = datetime.datetime.fromtimestamp(pdcs[i]["product_date"].timestamp())
            pdcs[i]["product_date"] = dt.replace(tzinfo=None)
        df = pandas.DataFrame(list(pdcs))
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=pdcs.xlsx'

        df.to_excel(response, index=False, engine='openpyxl')

        return response

class ExportPDCSToExcel(ExportExcel, View):
    def get(self, request, pid, *args, **kwargs):
        return self.get_records(pid)

    def get_records(self, pid=None):
        pdcs = ProductChanges.objects.filter(product_id=pid).values()
        return self.create_excel_file(pdcs, self.request)

class ExportPDSToExcel(ExportExcel, View):
    def get(self, request, *args, **kwargs):
        return self.get_records()

    def get_records(self, pid=None):
        pds = Products.objects.all().values()
        return self.create_excel_file(pds, self.request)