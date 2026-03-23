from django.db import models

# Create your models here.
from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='bandas')

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=150)
    localizacao = models.CharField(max_length=100)
    bandas = models.ManyToManyField(Banda, related_name='festivais')

    def __str__(self):
        return self.nome