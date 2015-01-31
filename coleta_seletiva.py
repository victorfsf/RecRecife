# -*- encoding: utf-8 -*-

import codecs
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RecRecife.settings")
django.setup()

from RecRecife.settings import STATIC_DIR, GOOGLE_API_SECRET_KEY
from recmap.models import Endereco, Horario, Coleta, Setor, ColetaHorario
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

    gmaps = googlemaps.Client(key=GOOGLE_API_SECRET_KEY)

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

            dias = line[5].split(',')
            for dia in dias:
                setor = Setor.objects.get_or_create(nome=line[1], frequencia=dias_dict[''.join(dia.split())])

            try:
                endereco = (Endereco.objects.get(csv_nome=line[2]), False)
                coleta = Coleta.objects.get_or_create(endereco=endereco[0], setor=setor[0], rota=line[4])
                coleta_horario = ColetaHorario.objects.get_or_create(horario=horario[0], coleta=coleta[0])

            except Endereco.DoesNotExist:

                try:
                    geocode = gmaps.geocode(line[2] + u' RECIFE PERNAMBUCO')
                    latitude = geocode[0]['geometry']['location']['lat']
                    longitude = geocode[0]['geometry']['location']['lng']

                    p_nome = line[2]
                    nome = line[2]
                    bairro = None

                    if not (latitude == -8.0578381 and longitude == -34.8828969):

                        geoindex = len(geocode[0]['address_components'])

                        for i in range(0, geoindex):

                            types = geocode[0]['address_components'][i]['types'][0]

                            if 'route' in types or 'bus_station' in types or 'transit_station' in types\
                                    or 'subway_station' in types or 'train_station' in types:

                                p_nome = geocode[0]['address_components'][i]['short_name']
                                nome = geocode[0]['address_components'][i]['long_name']

                            elif geocode[0]['address_components'][i]['types'][0] == 'neighborhood':

                                bairro = geocode[0]['address_components'][i]['long_name']

                    endereco = Endereco.objects.get_or_create(nome=nome, latitude=latitude, longitude=longitude,
                                                              p_nome=p_nome, bairro=bairro, csv_nome=line[2])

                    coleta = Coleta.objects.get_or_create(endereco=endereco[0], setor=setor[0], rota=line[4])
                    coleta_horario = ColetaHorario.objects.get_or_create(horario=horario[0], coleta=coleta[0])

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