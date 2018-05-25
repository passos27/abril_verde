from rest_framework import serializers
from .models import *


class PalestrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palestras
        depth = 1
        fields = ['id', 'titulo','descricao','dt_abertura','palestrante']


class PerguntaSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pergunta
        depth = 1
        fields = ['id', 'nome','cpf','email','pergunta','dt_pergunta','dt_atualizacao','status']
    def get_status(self,obj):
        return obj.get_status_display()