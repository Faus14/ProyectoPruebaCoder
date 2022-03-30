from django.contrib import admin

from .models import Entregable, Estudiante, Profesor, curso

# Register your models here.

admin.site.register(curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
