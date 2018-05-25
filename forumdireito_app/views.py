# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
# from rest_framework_api_key.permissions import HasAPIAccess
from django.template.response import TemplateResponse
from django.urls import reverse
from django.urls.base import reverse_lazy
from forumdireito_app.models import *

# dados

from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView



from django.shortcuts import render

# Create your views here.


class PalestrasList(APIView):
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (HasAPIAccess, )

    serializer_class = PalestrasSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Palestras.objects.all(), many=True)
        return Response(serializer.data)


class PerguntaList(APIView):
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (HasAPIAccess, )

    serializer_class = PerguntaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Pergunta.objects.filter(cpf=request.GET.get('cpf')), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response({"message:": "403 Forbiden"}, status=status.HTTP_409_CONFLICT)


class PalesranteList(APIView):
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (HasAPIAccess, )

    serializer_class = PalesranteSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Palestrante.objects.all(), many=True)
        return Response(serializer.data)


def PainelMediador(request):
    pergunta = Pergunta.objects.all()

    return render(request, 'painel.html', locals())