# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from forumdireito_app.models import *




# Register your models here.
class Palestrassadmin(admin.ModelAdmin):
    list_display = ['titulo', ]
    search_fields = ['palestras__titulo',]

class Palestranteadmin(admin.ModelAdmin):
    list_display = ['nome', ]
    search_fields = ['palestrante__nome', ]


class Perguntaadmin(admin.ModelAdmin):
    list_display = ['nome', ]
    search_fields = ['nome', ]

admin.site.register(Palestras, Palestrassadmin)
admin.site.register(Palestrante, Palestranteadmin)
admin.site.register(Pergunta, Perguntaadmin)