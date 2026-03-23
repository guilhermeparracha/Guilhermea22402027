from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente)
    favoritada_por = models.ManyToManyField('auth.User', related_name='receitas_favoritas')