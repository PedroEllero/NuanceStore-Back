from rest_framework import serializers
from.models import *

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('descricao','preco')

class Tipo(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('IDProduto', 'descricao')