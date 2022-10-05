from django.urls import path

from . import views

app_name = "aforo"

urlpatterns = [
    path('', views.list, name="list_aforo"),
    path('get/<str:id_rest>/', views.get, name="get_aforo"),
]
