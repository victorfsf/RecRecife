# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from RecRecife.settings import GOOGLE_API_SECRET_KEY
from recmap.models import Endereco
from django.db import connection
from recmap.methods import dictfetchall
from recmap.forms import FeedbackForm
from django.core.urlresolvers import reverse
import json


def view_index(request):
    args = {}
    enderecos = None
    q = None
    enderecos_json = []
    local = None
    setores = []
    start = False

    if request.method == 'POST':

        feedback_form = FeedbackForm(data=request.POST)

        if feedback_form.is_valid():

            feedback = feedback_form.save(commit=False)

            feedback.situacao = feedback_form.cleaned_data.get('erros')
            feedback.enviado_por = feedback_form.cleaned_data.get('nome')

            feedback.save()

        return HttpResponseRedirect(reverse('index') + '?s=1')
    else:
        feedback_form = FeedbackForm()
        cursor = connection.cursor()

        if 's' in request.GET:
            start_get = request.GET.get('s')

            if start_get == '1':
                start = True

        if 'q' in request.GET:
            q = request.GET.get('q')

            if q:

                query_str = "SELECT nome, nome_min, nome_bruto, bairro, latitude, longitude, " \
                            "intervalo, turno, nome_setor, rota, frequencia " \
                            "FROM recmap_endereco AS endr " \
                            "INNER JOIN recmap_coleta AS col ON endr.id = col.endereco_id " \
                            "INNER JOIN recmap_setor AS setor ON col.setor_id = setor.id " \
                            "INNER JOIN recmap_coletahorario AS ch ON ch.coleta_id = col.id " \
                            "INNER JOIN recmap_horario AS hor ON hor.id = ch.horario_id " \
                            "WHERE nome LIKE '%%%s%%' " \
                            "OR nome_min LIKE '%%%s%%' " \
                            "OR nome_bruto LIKE '%%%s%%' " \
                            "GROUP BY nome " \
                            "ORDER BY endr.id;"% (q, q ,q)

                cursor.execute(query_str)
                enderecos = dictfetchall(cursor)[:10]

        if 'l' in request.GET:
            l = request.GET.get('l')

            query_str = "SELECT nome, nome_min, nome_bruto, bairro, latitude, longitude, " \
                        "intervalo, turno, nome_setor, rota, frequencia " \
                        "FROM recmap_endereco AS endr " \
                        "INNER JOIN recmap_coleta AS col ON endr.id = col.endereco_id " \
                        "INNER JOIN recmap_setor AS setor ON col.setor_id = setor.id " \
                        "INNER JOIN recmap_coletahorario AS ch ON ch.coleta_id = col.id " \
                        "INNER JOIN recmap_horario AS hor ON hor.id = ch.horario_id " \
                        "WHERE endr.nome = '%s'" % l

            cursor.execute(query_str)

            try:
                setores = dictfetchall(cursor)
                local = setores[0]

                if local['nome'] == local['nome_bruto'] and local['nome_min'] == local['nome_bruto']:
                    local['warning'] = True
                else:
                    local['warning'] = False
            except IndexError:
                pass

        cursor.close()

    list_enderecos = Endereco.objects.iterator()

    for endereco in list_enderecos:
        endereco.__dict__.pop('_state', None)
        enderecos_json.append(endereco.__dict__)

    markers_json = json.dumps(enderecos_json)

    args['first_time'] = not start
    args['feedback_form'] = feedback_form
    args['local'] = local
    args['setores'] = setores
    args['markers'] = markers_json
    args['query_data'] = q
    args['enderecos'] = enderecos
    args['GOOGLE_API_SECRET_KEY'] = GOOGLE_API_SECRET_KEY

    return render(request, 'recmap/index.html', args)
