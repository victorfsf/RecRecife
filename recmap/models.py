# -*- encoding: utf-8 -*-

from django.db import models


class Endereco(models.Model):
    nome_bruto = models.CharField(max_length=100)
    nome_min = models.CharField(max_length=200)
    nome = models.CharField(max_length=200, unique=True)
    bairro = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.nome) + u' (' + unicode(self.bairro) + u')'

    class Meta:
        verbose_name = u'endereço'
        verbose_name_plural = u'endereços'


class Horario(models.Model):
    turno = models.CharField(max_length=15)
    intervalo = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.intervalo) + u' (' + unicode(self.turno) + u')'

    class Meta:
        verbose_name = u'horário'
        verbose_name_plural = u'horários'


class Setor(models.Model):
    nome_setor = models.CharField(max_length=10)
    frequencia = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.nome_setor)

    class Meta:
        verbose_name = u'setor'
        verbose_name_plural = u'setores'


class Coleta(models.Model):
    endereco = models.ForeignKey(Endereco)
    setor = models.ForeignKey(Setor)
    rota = models.IntegerField(max_length=5)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.endereco) + u' - ' + unicode(self.setor) + u', Rota: ' + unicode(self.rota)

    class Meta:
        verbose_name = u'coleta'
        verbose_name_plural = u'coletas'


class ColetaHorario(models.Model):
    coleta = models.ForeignKey(Coleta)
    horario = models.ForeignKey(Horario)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.coleta) + u' - ' + unicode(self.horario)

    class Meta:
        verbose_name = u'coleta/Horário'
        verbose_name_plural = u'coleta/horários'


class Feedback(models.Model):
    enviado_por = models.CharField(max_length=200, default='Anônimo')
    email = models.EmailField(max_length=256, default='None')
    situacao = models.CharField(max_length=256)
    descricao = models.TextField(max_length=512, default='Sem descrição!')
    ativo = models.BooleanField(default=True)
    resolvido = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.enviado_por) + ' - ' + unicode(self.situacao)

    class Meta:
        verbose_name = u'Feedback'
        verbose_name_plural = u'Feedbacks'