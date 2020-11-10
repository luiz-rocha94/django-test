from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('biografia', views.biografia, name='biografia'),
    path('campanhas-publicitarias', views.campanhas_publicitarias, name='campanhas-publicitarias'),
    path('contato', views.contato, name='contato'),
]