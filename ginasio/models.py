from django.db import models

# Create your models here.
class PT(models.Model):
    nome = models.CharField(max_length=100)

class Membro(models.Model):
    nome = models.CharField(max_length=100)

class Sessao(models.Model):
    pt = models.ForeignKey(PT, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        unique_together = ('pt', 'data', 'hora')