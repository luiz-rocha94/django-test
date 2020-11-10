from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'polls2/index.html')

def campanhas_publicitarias(request):
    return render(request, 'polls2/campanhas-publicitarias.html')

def biografia(request):
    return render(request, 'polls2/biografia.html')

def contato(request):
    return render(request, 'polls2/contato.html')
