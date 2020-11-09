from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')

def quem_somos(request):
    return render(request, 'polls/quem-somos.html')

def contato(request):
    if request.method == 'POST':
        pass
    return render(request, 'polls/contato.html')