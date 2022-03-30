
from django.urls import path

from .views import curso1, entregables, estudiantes, inicio, profesores


urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregacurso/<nombre>/<canada>', curso1),
    path('profesores', profesores, name="profesores"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path('entregables', entregables, name="entregables"),
    
]
