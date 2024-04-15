from django.db import models

# Create your models here.

#  class Tipo(models.Model):
#      descricao = models.CharField(max_length=50)

class Produto(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=12)
    descricao = models.CharField(max_length=200)
    Tipo = models.CharField(max_length=50)
#   IDTipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)