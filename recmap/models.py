# -*- encoding: utf-8 -*-

from django.db import models


class Endereco(models.Model):
    csv_nome = models.CharField(max_length=100)
    p_nome = models.CharField(max_length=200)
    nome = models.CharField(max_length=200, unique=True)
    bairro = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return unicode(self.nome) + u' (' + unicode(self.bairro) + u')'

    class Meta:
        verbose_name = u'endereço'
        verbose_name_plural = u'endereços'


class Horario(models.Model):
    turno = models.CharField(max_length=15)
    intervalo = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return unicode(self.intervalo) + u' (' + unicode(self.turno) + u')'

    class Meta:
        verbose_name = u'horário'
        verbose_name_plural = u'horários'


class Setor(models.Model):
    nome = models.CharField(max_length=10)
    frequencia = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.nome)

    class Meta:
        verbose_name = u'setor'
        verbose_name_plural = u'setores'


class Coleta(models.Model):
    endereco = models.ForeignKey(Endereco)
    setor = models.ForeignKey(Setor)
    rota = models.IntegerField(max_length=5)

    def __unicode__(self):
        return unicode(self.endereco) + u' - ' + unicode(self.setor) + u', Rota: ' + unicode(self.rota)

    class Meta:
        verbose_name = u'coleta'
        verbose_name_plural = u'coletas'


class ColetaHorario(models.Model):
    coleta = models.ForeignKey(Coleta)
    horario = models.ForeignKey(Horario)

    def __unicode__(self):
        return unicode(self.coleta) + u' - ' + unicode(self.horario)

    class Meta:
        verbose_name = u'coleta/Horário'
        verbose_name_plural = u'coleta/horários'

