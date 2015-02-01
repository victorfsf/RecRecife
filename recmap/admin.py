# -*- encoding: utf-8 -*-

from django.contrib import admin
from recmap.models import Endereco, Horario, Coleta, Setor, ColetaHorario, Feedback


class EnderecoAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Nome da Rua', {'fields': ('nome_bruto', 'nome_min', 'nome')}),
        (u'Bairro / Geolocalização', {'fields': ('bairro', 'latitude', 'longitude')}),
    )

    list_display = ('nome', 'bairro', 'latitude', 'longitude', 'nome_bruto')
    search_fields = ('nome', 'bairro', 'latitude', 'longitude', 'nome_bruto', 'nome_min')


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
    search_fields = ('endereco__nome', 'endereco__bairro', 'setor__nome_setor', 'setor__frequencia', 'rota',)


class ColetaHorarioAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Informações', {'fields': ('coleta', 'horario',)}),
    )

    list_display = ('coleta', 'horario',)
    search_fields = ('coleta__endereco__nome', 'coleta__endereco__bairro', 'horario__turno', 'horario__intervalo')


class SetorAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Informações', {'fields': ('nome_setor', 'frequencia',)}),
    )

    list_display = ('nome_setor', 'frequencia',)
    search_fields = ('nome_setor', 'frequencia',)


class FeedbackAdmin(admin.ModelAdmin):

    fieldsets = (
        (u'Informações', {'fields': ('enviado_por', 'email', 'situacao', 'descricao',)}),
    )

    list_display = ('enviado_por', 'email', 'situacao', 'descricao',)
    search_fields = ('nome', 'email', 'situacao', 'descricao',)


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Coleta, ColetaAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(ColetaHorario, ColetaHorarioAdmin)
admin.site.register(Feedback, FeedbackAdmin)