from django.db import models

# Create your models here.
from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    grau = models.CharField(max_length=50, default="Licenciatura")
    ects = models.IntegerField(default=180)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    link_docente_lusofona = models.URLField(blank=True)
    # A relação que decidiste: uma UC pode estar em várias Licenciaturas
    licenciaturas = models.ManyToManyField(Licenciatura, related_name='unidades_curriculares')

    def __str__(self):
        return self.nome