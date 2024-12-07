from django.db import models

class PlanoTreino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor_mensal = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    plano = models.ForeignKey(PlanoTreino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
