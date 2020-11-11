from django.shortcuts import render

def index(request):
    return render(request, 'polls4/index.html')
