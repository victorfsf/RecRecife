# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from RecRecife.settings import GOOGLE_API_SECRET_KEY
from recmap.models import Endereco
from django.db.models import Q
import json


def view_teste(request):
    args = {}
    enderecos = None
    q = None
    enderecos_json = []

    if request.method == 'GET':

        if 'q' in request.GET:
            q = request.GET.get('q')

            if q:
                endereco_startswith = Q(nome__istartswith=q) | Q(p_nome__istartswith=q) | Q(csv_nome__istartswith=q)
                endereco_contains = Q(nome__icontains=q) | Q(p_nome__icontains=q) | Q(csv_nome__icontains=q)

                enderecos = Endereco.objects.filter(endereco_startswith)

                if not enderecos:
                    enderecos = Endereco.objects.filter(endereco_contains)

                enderecos = enderecos[:10]

    for endereco in Endereco.objects.all().order_by('id'):
        endereco.__dict__.pop('_state', None)
        enderecos_json.append(endereco.__dict__)

    markers_json = json.dumps(enderecos_json)

    args['markers'] = markers_json
    args['query_data'] = q
    args['enderecos'] = enderecos
    args['GOOGLE_API_SECRET_KEY'] = GOOGLE_API_SECRET_KEY

    return render(request, 'recmap/test.html', args)
