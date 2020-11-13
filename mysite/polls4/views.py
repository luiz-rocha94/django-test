from django.shortcuts import render

def index(request):
    return render(request, 'polls4/index.html')

def brasil(request):
    return render(request, 'polls4/brasil.html')

def fotos(request):
    return render(request, 'polls4/fotos.html')

def nova_legislacao(request):
    return render(request, 'polls4/nova-legislacao.html')