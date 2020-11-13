from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('brasil', views.brasil, name='brasil'),
    path('fotos', views.fotos, name='fotos'),
    path('nova-legislacao', views.nova_legislacao, name='nova-legislacao'),
]