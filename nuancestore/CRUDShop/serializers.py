from rest_framework import serializers
from.models import *

# class Tipo(serializers.ModelSerializer):
#     class Meta:
#         model = Tipo
#         fields = ('descricao')

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            # 'IDTipo',
            'descricao',
            'preco',
            'Tipo'
            )
