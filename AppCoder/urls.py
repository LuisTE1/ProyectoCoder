from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('curso/',views.curso, name="Cursos"),
 

]
