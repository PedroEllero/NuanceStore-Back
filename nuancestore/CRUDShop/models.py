from django.db import models

# Create your models here.

class Tipo(models.Model):
    IDTipo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)

class Produto(models.Model):
    IDProduto = models.AutoField(primary_key=True)
    preco = models.DecimalField(decimal_places=2, max_digits=12)
    descricao = models.CharField(max_length=200)
    IDTipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)