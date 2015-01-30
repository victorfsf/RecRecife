# -*- encoding: utf-8 -*-

from django.contrib import admin
from recmap.models import Endereco, Horario, Coleta, Setor

admin.site.register(Endereco)
admin.site.register(Horario)
admin.site.register(Coleta)
admin.site.register(Setor)