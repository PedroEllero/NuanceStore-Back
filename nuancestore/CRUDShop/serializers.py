from rest_framework import serializers
from.models import *

class Tipo(serializers.ModelSerializer):
     class Meta:
         model = Tipo
         fields = ('categoria')

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'IDTipo',
            'descricao',
            'preco',
            'Tipo',
            'nome',
            )
