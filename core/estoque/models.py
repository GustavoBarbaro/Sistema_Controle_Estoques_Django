from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    tag_rfid = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome


class Usuario (AbstractUser):
    tag_rfid = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    data = models.DateField()

    def __str__(self):
        return f'{self.tipo} - {self.produto.nome}'

