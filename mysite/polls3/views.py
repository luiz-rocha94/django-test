from django.shortcuts import render

def index(request):
    return render(request, 'polls3/index.html')