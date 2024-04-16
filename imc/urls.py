from django.urls import path
from . import views

app_name = 'imc'
urlpatterns = [
    path('',views.calculate,name='calculate')
]
