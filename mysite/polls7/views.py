from django.shortcuts import render

def index(request):
    return render(request, 'polls7/index.html')

