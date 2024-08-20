from django.db import models
from ckeditor.fields import RichTextField

class Cursos(models.Model):  # Define la estructura de nuestra tabla
    nombreCurso = models.TextField()  # Texto largo
    des = models.TextField(verbose_name="Descripcion del curso")
    aprendizaje = RichTextField(verbose_name="Lista de aprendizaje")
    costo = models.CharField(max_length=15)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen")
    calificacion = models.CharField(max_length=5, verbose_name="Calificación")
    inscritos = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
        # El menos indica que se ordenara del más reciente al mas viejo
        #Sin el signo menos se  ordenara del más antiguo al más reciente 

    def __str__(self):
        return self.nombreCurso

class PreInscripcion(models.Model):  # Nombre de la clase en CamelCase
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.TextField(verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo")  # Cambiado a EmailField
    curso = models.TextField(verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = "Pre-Inscripciones"
        verbose_name_plural = "Pre-Inscripciones"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre




