from django.urls import path, include
from . import views

urlpatterns = [
    path('listar/', views.ListarApiView.as_view()),

]
