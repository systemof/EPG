#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function  # Compatibilidade com print no Python 2.7 e 3.x
import sys
import unicodedata
import re
import os
import glob
import gzip
from datetime import datetime

# Verifique a versão do Python para lidar com diferenças entre Python 2 e 3
if sys.version_info[0] < 3:
    input = raw_input  # No Python 2, raw_input() é equivalente a input() no Python 3
    unicode_type = unicode  # No Python 2, use unicode para strings
else:
    unicode_type = str  # No Python 3, todas as strings são unicode por padrão

def main():
    lamedb = "/etc/enigma2/lamedb"
    piconLocations = [
        "/usr/share/enigma2/picon/", "/picon/", "/media/usb/picon/", "/media/usb2/picon/",
        "/media/hdd/picon/", "/media/hdd2/picon/", "/media/cf/picon/", "/media/sdb/picon/",
        "/media/sdb2/picon/", "/media/sda/picon/"
    ]
    canaisxml = "/tmp/.canais.xml"
    paths = []
    pattern = "*.png"
    print("Procurando por Referencias...")

    # Localizar todos os arquivos de ícones de picon
    for l in piconLocations:
        paths = paths + glob.glob(l + pattern)
    pathsSplit = []
    for p in paths:
        pathsSplit.append(p.rsplit('/', 1))
    paths = {}
    print("Processando Arquivos...")

    for p in pathsSplit:
        f = p[0] + '/' + p[1]
        n = p[1]
        if os.path.islink(f):
            f = p[0] + '/' + os.readlink(f)
            if os.path.exists(f):
                paths[n] = f
        else:
            paths[n] = f

    try:
        with open(lamedb, 'r') as f:
            lines = f.readlines()
            lines = lines[lines.index("services\n") + 1:-3]
    except Exception as e:
        print("Erro ao ler o arquivo lamedb: {}".format(e))
        sys.exit(1)

    i = 0
    messages = []
    try:
        with open(canaisxml, 'w') as arquivo:
            while len(lines) > 2:
                ref = [x for x in lines[0][:-1].split(':')]
                name = lines[1][:-1]
                lines = lines[3:]  # para a próxima iteração
                slot = slot1(ref[1])
                sat = slot1(ref[1])
                refstr = "1:0:1:%x:%x:%x:%x:0:0:0" % (int(ref[0], 0x10), int(ref[2], 0x10), int(ref[3], 0x10), int(ref[1], 0x10))
                serviceType = str(hex(int(ref[4]))).replace('0x', '')
                refstr2 = "1:0:%s:%x:%x:%x:%x:0:0:0" % (serviceType, int(ref[0], 0x10), int(ref[2], 0x10), int(ref[3], 0x10), int(ref[1], 0x10))

                # Processamento dos nomes dos canais
                Nomes1 = unicodedata.normalize('NFC', unicode_type(name, 'utf_8')).encode('latin-1', 'ignore').decode('latin-1').replace('&', '&amp;').replace(' ', '').upper()
                newPiconName = Nomes1

                if int(ref[4]) < 26:  # tipo de serviço em decimal
                    if (len(newPiconName) and newPiconName in paths) or refstr in paths or refstr2 in paths:
                        finished = True
                    else:
                        messages.append((Nomes1, newPiconName, refstr2, sat, int(ref[4])))
                i += 1
                if i % 100 == 0:
                    print("Lendo {} Canais... Encontrados".format(i))

            # Escrever o arquivo XML
            log1 = ''
            for message in messages:
                log1 += '\t\t<channel id="%s">%s:</channel> <!-- %s - %s -->\n' % (
                    message[0], message[2], message[3], message[4]
                )
            arquivo.write(log1)
        print("Arquivo .canais.xml gerado com sucesso.")
    except Exception as e:
        print("Erro ao escrever o arquivo .canais.xml: {}".format(e))
        sys.exit(1)

    print("Finalizando...")
    try:
        datahoje = datetime.now().strftime('Gerado em %d/%m/%Y  %H:%M:%S')
        cabecalho_path = '/tmp/.cabecalho.xml'
        with open(cabecalho_path, "w") as cabecalho:
            cabecalho.write('<?xml version="1.0" encoding="latin-1"?>\n\t<!-- %s -->\n\t<channels>\n' % datahoje)

        channels_xml_path = '/tmp/channels.xml'
        with open(channels_xml_path, 'w') as outfile:
            for fname in [cabecalho_path, canaisxml]:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
            outfile.write('\t</channels>')

        os.system("cp /tmp/channels.xml /etc/enigma2/ &> /dev/null")
        os.system("gzip -k /etc/enigma2/channels.xml &> /dev/null")
        print("Arquivo channels.xml copiado e compactado com sucesso.")
    except Exception as e:
        print("Erro ao finalizar o arquivo channels.xml: {}".format(e))
        sys.exit(1)

def slot1(namespace):
    return int(namespace[:len(namespace) - 4], 16)

if __name__ == '__main__':
    main()
