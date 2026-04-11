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


class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    site_oficial = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(help_text="Escala de 1 a 5")

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    github_url = models.URLField(blank=True)
    video_link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    # Ligação à Licenciatura
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='formacoes')

    def __str__(self):
        return f"{self.curso} ({self.instituicao})"


class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    orientador = models.CharField(max_length=100)
    ano = models.IntegerField()
    resumo = models.TextField()
    link_relatorio = models.URLField(blank=True)
    e_favorito = models.BooleanField(default=False) # Para destacar os de maior interesse

    def __str__(self):
        return self.titulo