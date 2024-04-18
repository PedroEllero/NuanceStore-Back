from django.db import models

# Create your models here.
class Endereco(models.Model):
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=20)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cep = models.IntegerField()
    
    def __str__(self):
        return str((self.cidade, self.estado, self.logradouro, self.bairro, self.numero, self.cep))
    
class User(models.Model):
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=50)
    email = models.EmailField(error_messages="ERRO: e-mail fornecido não é valido")
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=30)
    enderecos = models.ManyToManyField(Endereco)

    def __str__(self):
        return self.cpf