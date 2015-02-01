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
    'DIÁRIA': u'Diária',
}

"""
ENDEREÇO(NOME, NOME_MIN, NOME_CSV, BAIRRO, LAT, LONG)
SETOR(ID, FREQUÊNCIA)
COLETA(ID, NOME_ENDERECO, SETOR_ID, NUM_ROTA)
HORARIO(TURNO, INTERVALO)
COLETA_HORARIO(ID_COLETA, INTERVALO)
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