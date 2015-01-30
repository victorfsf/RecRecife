# -*- encoding: utf-8 -*-

import codecs
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RecRecife.settings")
django.setup()

from RecRecife.settings import STATIC_DIR
from recmap.models import Endereco, Horario, Coleta, Setor, HorarioSetor
from django.db.utils import IntegrityError
from datetime import datetime
from googlemaps import googlemaps

dias_dict = {
    'SEG': 'Segunda',
    'TER': u'Terça',
    'QUA': 'Quarta',
    'QUI': 'Quinta',
    'SEX': 'Sexta',
    'SAB': U'Sábado',
    'DIARIA': u'Diária',
}

"""
ENDEREÇO(RUA, LAT, LONG)
SETOR(ID, FREQUÊNCIA)
PASSA(LAT, LONG, SETOR_ID)
HORARIO(TURNO, INTERVALO)
HORARIO_SETOR(ID_SETOR, INTERVALO)
ROTA(NUM_ROTA, SETOR_ID)
"""

if __name__ == '__main__':

    inicio = datetime.now()

    gmaps = googlemaps.Client(key='AIzaSyAPQDn0IzFxC1lOe_Ipg9hcY6jZ78EQVKU')

    with codecs.open(STATIC_DIR + '\\recrecife\\csv\\roteirizacao.csv', 'r', 'utf-8') as f:
        f.next()
        counter = 0
        not_found = 0
        for line in f:
            line = line.split(';')

            try:
                horario = Horario.objects.get_or_create(intervalo=line[0], turno=line[3].lower().title())
            except IntegrityError:
                horario = Horario.objects.get_or_create(intervalo=line[0])

            setor = Setor.objects.get_or_create(nome=line[1], frequencia=line[5])
            horario_setor = HorarioSetor.objects.get_or_create(intervalo=horario[0], setor=setor[0])

            try:
                endereco = (Endereco.objects.get(csv_nome=line[2]), False)
                coleta = (line[2] + u' - ' + unicode(setor[0]), False)
            except Endereco.DoesNotExist:

                try:
                    geocode = gmaps.geocode(line[2] + u' RECIFE PERNAMBUCO')
                    latitude = geocode[0]['geometry']['location']['lat']
                    longitude = geocode[0]['geometry']['location']['lng']
                    p_nome = geocode[0]['address_components'][0]['short_name']
                    nome = geocode[0]['address_components'][0]['long_name']
                    bairro = geocode[0]['address_components'][1]['long_name']

                    endereco = Endereco.objects.get_or_create(nome=nome, latitude=latitude, longitude=longitude,
                                                                  p_nome=p_nome, bairro=bairro, csv_nome=line[2])
                    coleta = Coleta.objects.get_or_create(endereco=endereco[0], setor=setor[0], rota=line[4])

                except IndexError:
                    not_found += 1
                    endereco = (line[2], False)
                    coleta = (line[2] + u' - ' + unicode(setor[0]), False)

            counter += 1

            print unicode(counter) + u' - ' + unicode(horario[0]) + u', ' + unicode(horario[1])
            print unicode(counter) + u' - ' + unicode(setor[0]) + u', ' + unicode(setor[1])
            print unicode(counter) + u' - ' + unicode(endereco[0]) + u', ' + unicode(endereco[1])
            print unicode(counter) + u' - ' + unicode(coleta[0]) + u', ' + unicode(coleta[1])

    fim = datetime.now()

    print 'Falhas: ' + unicode(not_found)
    print fim - inicio