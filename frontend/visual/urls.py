from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('mecanico_list', views.mecanico_list , name='mecanico_list'),

]