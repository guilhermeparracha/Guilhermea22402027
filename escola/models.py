from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=10)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE)

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')