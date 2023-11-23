from django.urls import path,include
from rest_framework import routers
from api_mecanico import views

router=routers.DefaultRouter()
router.register(r'registro_mecanico',views.Registro_mecViewSet)

urlpatterns=[
    path('',include(router.urls))   
]