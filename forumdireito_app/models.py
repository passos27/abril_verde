# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

STATUS_PERGUNTA = (
    ('0', 'Aguardando Resposta'),
    ('2', 'Respondido'),
    ('3', 'Cancelado'),
)

class Palestrante(models.Model):
    nome = models.CharField(u'Título', max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to='palestrante', null=True, blank=True)
    curriculo = models.TextField(u'Mini currículo', max_length=140, null=True, blank=True)
    dt_abertura = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = u'Palestrante'
        verbose_name_plural = u'Palestrantes'
    def __unicode__(self):
        return u'%s' % self.nome



class Palestras(models.Model):
    palestrante = models.ForeignKey(Palestrante,on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(u'Título', max_length=100, null=True, blank=True)
    descricao = models.TextField(u'Descreva a palestra', max_length=140, null=True, blank=True)
    dt_abertura = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = u'Palestra'
        verbose_name_plural = u'Palestras'
    def __unicode__(self):
        return u'%s' % self.titulo


class Pergunta(models.Model):
    nome = models.CharField(u'Nome', max_length=100, null=True, blank=True)
    cpf = models.CharField(u'CPF', max_length=100, null=True, blank=True)
    email = models.CharField(u'E-mail', max_length=100, null=True, blank=True)
    pergunta = models.TextField(u'Pergunta', max_length=140, null=True, blank=True)
    dt_pergunta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(u'Status', max_length=140,  choices=STATUS_PERGUNTA, default=0, null=True, blank=True)

    class Meta:
        verbose_name = u'Pergunta'
        verbose_name_plural = u'Perguntas'
    def __unicode__(self):
        return u'%s' % self.nome