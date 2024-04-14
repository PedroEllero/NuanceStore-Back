from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('cpf','nome','email','telefone')
    

class Endereco(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('UserCpf','cidade','estado','logradouro','numero','bairro','cep')