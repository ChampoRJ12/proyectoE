from django.contrib import admin
from .models import Cursos   # Asegúrate de usar el nombre correcto del modelo
from .models import PreInscripcion
class AdministrarCursos(admin.ModelAdmin):
    list_display = ('nombreCurso', 'des', 'costo', 'created')
    search_fields = ('nombreCurso', 'des')
    readonly_fields = ('created', 'updated')

admin.site.register(Cursos, AdministrarCursos)

class AdministrarPreInscripciones(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'curso')
    search_fields = ('nombre', 'correo', 'curso')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(PreInscripcion, AdministrarPreInscripciones)
