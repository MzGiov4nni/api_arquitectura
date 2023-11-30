from django.urls import path
from api_mecanico import views

urlpatterns=[

    path('', views.Lista_mecanico, name="Mecanicos"),
    path('detalle/<str:pk>', views.Detalle_Mecanico, name="Detalle_Mecanico"),
    path('crear', views.Crear_registro, name="Registrar_Mecanico"),
    path('actualizar/<str:pk>/', views.Actualizar_mecanico, name="Actualizar_Mecanico"),
    path('eliminar/<str:pk>/', views.Eliminar_mecanico, name="Eliminar_Mecanico"),
]