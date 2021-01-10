from django.urls import path
from .views import home, datos, resultados 

urlpatterns = [
    path('', home, name="home"),
    path('datos/', datos, name="datos"),
    path('resultados/', resultados, name="resultados"),
]