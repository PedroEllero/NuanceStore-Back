from django.db import models

# Create your models here.

class User(models.Model):
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.cpf
    
class Endereco(models.Model):
    UserCpf = models.ForeignKey(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=20)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cep = models.IntegerField()
    