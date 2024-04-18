from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('cpf','nome','email','telefone', 'senha', 'enderecos')
    

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('cidade','estado','logradouro','numero','bairro','cep')