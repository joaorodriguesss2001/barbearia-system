from django.db import models

# Create your models here.

# Tabela de Barbeiros

class Barbeiro(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100, blank=True) # Ex Barba, Corte

    def __str__(self):
        return self.nome
    
# Tabela de Clientes

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
# Tabela de Agendamentos

class Agendamento(models.Model):

    nome_cliente = models.CharField(max_length=100, default="")
    telefone_cliente = models.CharField(max_length=20, default="")
    
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, default='A') # A de Agendado

    def __str__(self):
        return f"{self.nome_cliente} - {self.data_hora}"
