# -*- encoding: utf-8 -*-

from django.contrib import admin
from recmap.models import Endereco, Horario, Coleta, Setor, ColetaHorario


class EnderecoAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Nome da Rua', {'fields': ('csv_nome', 'p_nome', 'nome')}),
        (u'Bairro / Geolocalização', {'fields': ('bairro', 'latitude', 'longitude')}),
    )

    list_display = ('nome', 'bairro', 'latitude', 'longitude', 'csv_nome')
    search_fields = ('nome', 'bairro', 'latitude', 'longitude', 'csv_nome', 'p_nome')


class HorarioAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Horário', {'fields': ('intervalo', 'turno')}),
    )

    list_display = ('intervalo', 'turno',)
    search_fields = ('intervalo', 'turno',)


class ColetaAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Informações da coleta', {'fields': ('endereco', 'setor', 'rota')}),
    )

    list_display = ('endereco', 'setor', 'rota',)
    search_fields = ('endereco', 'setor', 'rota',)


class ColetaHorarioAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Informações', {'fields': ('coleta', 'horario',)}),
    )

    list_display = ('coleta', 'horario',)
    search_fields = ('coleta', 'horario',)


class SetorAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Informações', {'fields': ('nome', 'frequencia',)}),
    )

    list_display = ('nome', 'frequencia',)
    search_fields = ('nome', 'frequencia',)


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Coleta, ColetaAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(ColetaHorario)