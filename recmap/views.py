# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect


def view_teste(request):
    args = {}

    if request.method == 'GET':

        if 'q' in request.GET:
            print request.GET

    args['query'] = request.GET.get('q')
    return render(request, 'recmap/test.html', args)
