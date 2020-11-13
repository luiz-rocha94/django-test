from django.shortcuts import render

def index(request):
    return render(request, 'polls5/index.html')
