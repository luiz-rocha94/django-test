from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('quem-somos', views.quem_somos, name='quem-somos'),
    path('contato', views.contato, name='contato'),
]