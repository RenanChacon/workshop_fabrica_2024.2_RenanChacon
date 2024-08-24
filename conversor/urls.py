from django.urls import path
from . import views

urlpatterns = [
    path('mostrar_conversor/', views.mostrar_conversor, name="mostrar_conversor")
]