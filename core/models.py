from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_aluno
    