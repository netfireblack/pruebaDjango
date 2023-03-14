from django.contrib import admin
from .models import Alumno
from .models import Asignatura
from .models import Nota
from .models import Semestre

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Nota)
admin.site.register(Semestre)