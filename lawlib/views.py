from django.shortcuts import render
from django.views import generic

from .models import  Document,Provision,Rule,TaxReturn
# Create your views here.
def index(request):
    num_docs = Document.objects.all().count()
    num_provs = Provision.objects.all().count()
    num_rules = Rule.objects.all().count()
    num_val_rules = Rule.objects.filter(status__exact='I').count()
    num_taxreturns = TaxReturn.objects.all().count()

    context = {
        'num_docs': num_docs,
        'num_provs': num_provs,
        'num_rules': num_rules,
        'num_val_rules': num_val_rules,
        'num_taxreturns':num_taxreturns,
    }

    return render(request,'index.html',context)

class DocumentListView(generic.ListView):
    model = Document

class TaxReturnListView(generic.ListView):
    model = TaxReturn

class TaxReturnDetailView(generic.DetailView):
    model = TaxReturn

class DocumentDetailView(generic.DetailView):
    model = Document

class ProvisionListView(generic.ListView):
    model = Provision

class ProvisionDetailView(generic.DetailView):
    model = Provision

