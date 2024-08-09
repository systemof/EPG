#!/usr/bin/python
# -*- coding: utf-8 -*-
#<?xml version="1.0" encoding="utf-8"?>
#<!-- service references can be found in /etc/enigma2/lamedb -->
#<channels>
#<channel id="playboyhd">1:0:19:5EF:14:C9:BAE0000:0:0:0:</channel>
#</channels>
#FILE = "/etc/enigma2/lamedb"

import sys, unicodedata, re, os, glob, zipfile, time, datetime, gzip
def main():
        # lamedb = open(FILE, 'r').readlines()
        lamedb = "/etc/enigma2/lamedb"
        #lamedb = "/tmp/lamedb"
        piconLocations = ["/usr/share/enigma2/picon/", "/picon/", "/media/usb/picon/", "/media/usb2/picon/",
                          "/media/hdd/picon/", "/media/hdd2/picon/", "/media/cf/picon/", "/media/sdb/picon/",
                          "/media/sdb2/picon/", "/media/sda/picon/", ]
        canaisxml = "/tmp/.canais.xml"
        outlog1 = ".found-picons"
        outlog2 = "ch"
        outlog3 = ".impossible-picons"
        logExt = ".xml"
        piconOutFolder = "/picon/"
        # nomes = "/tmp/nomes"
        messages1 = []
        messages2 = {}
        messages3 = []
        # messages = {}
        messages = []
        paths = []
        pattern = "*.png"
        serviceTypes = []
        # self["status"].setText(_("PROCURANDO CANAIS E REFERENCIAS..."))
        print("PROCURANDO CANAIS E REFERENCIAS...")
        #	print "Procurando por Referencias ..."
        for l in piconLocations:
            paths = paths + glob.glob(l + pattern)
        pathsSplit = []
        for p in paths:
            pathsSplit.append(p.rsplit('/', 1))
        del (paths)
        paths = {}
        #	print "Processando Arquivos...\n"
        for p in pathsSplit:
            # parts = p[1].split('_', 3)
            f = p[0] + '/' + p[1]
            # n = "1_0_*_%s" % (parts[3])
            n = p[1]
            if os.path.islink(f):
                f = p[0] + '/' + os.readlink(f)
                if os.path.exists(f):
                    paths[n] = f
            else:
                paths[n] = f
        del (pathsSplit)
        print("Processando Arquivos...")
        #	print " "
        # f = open(lamedb).readlines()
        f = open(lamedb).readlines()
        f = f[f.index("services\n")+1:-3]
        i = 0
        done = []
        arquivo = open(canaisxml,'w')
        #zf = zipfile.ZipFile(outfile, mode='w', compression=zipfile.ZIP_DEFLATED)
        while len(f) > 2:
            ref = [x for x in f[0][:-1].split(':')]
            name = f[1][:-1]
            f = f[3:]  # for next iteration
            slot = slot1(ref[1])
            sat = slot1(ref[1])
            # if sat not in (130,192,282):
            #	continue
            refstr = "1:0:1:%x:%x:%x:%x:0:0:0" % (int(ref[0], 0x10), int(ref[2], 0x10), int(ref[3], 0x10), int(ref[1], 0x10))
            serviceType = str(hex(int(ref[4]))).replace('0x', '')  # just for the log
            refstr2 = "1:0:%s:%x:%x:%x:%x:0:0:0" % (serviceType, int(ref[0], 0x10), int(ref[2], 0x10), int(ref[3], 0x10),int(ref[1], 0x10))  # just for the log
            # ref = f[0][:-1] # service ref string from lamedb
            oldPiconName = refstr + "</channel>"
            #OrdemAZ = re.sub('[^a-z0-9]', ' ',SemAcentos) # ORDEM DE A a Z
            oldPiconName2 = refstr2   # TIRA O PNG DA EXTENCAO


            #ORIGINAL COM & e amp;

            Nomes1 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('ASCII', 'ignore').replace("MTV's 00", 'MTV00').replace(' HD', '').replace('&', '').replace('', '').replace(' ','').replace('/' ,'').replace('-' ,'').replace('' ,'').replace('.','').replace('(','').replace(')','').replace('+','PLUS').replace('!', '').replace('  ', ' ').upper()# COM ACENTOS
            Nomes2 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '&amp;').replace('', '').replace('  ', ' ')# COM ACENTOS
            Nomes3 = unicodedata.normalize('NFC', unicode(name, 'latin_1')).encode('latin-1', 'strict').replace('&', '&amp;').replace('', '').replace('  ', ' ')# COM ACENTOS
            newName1 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '&amp;').replace('', '').replace('  ', ' ')# COM ACENTOS
            newName2 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '&amp;').replace('', '').replace('  ', ' ')# COM ACENTOS

            #REMOVE & e amp;

            #Nomes1 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '').replace('&amp;', '').replace('amp;', '') # COM ACENTOS
            #Nomes2 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '').replace('&amp;', '').replace('amp;', '') # COM ACENTOS
            #Nomes3 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '').replace('&amp;', '').replace('amp;', '') # COM ACENTOS
            #newName1 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '').replace('&amp;', '').replace('amp;', '') # COM ACENTOS
            #newName2 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).encode('latin-1', 'ignore').replace('&', '').replace('&amp;', '').replace('amp;', '') # COM ACENTOS


            # REMOVER ACENTOS E UNIR CANAIS HD E SD EM UM SO ID CHANNEL.
            #Nomes1 = unicodedata.normalize('NFKD', unicode(name, 'utf_8')) # COM ACENTOS

            #newName1 = unicodedata.normalize('NFC', unicode(name, 'utf_8')).replace('&', '&amp;').replace(' ', '').upper()
            #newName2 = newName1.replace('&', '&').replace('+', '+').replace('*', '*').lower())

            #Nomes2 = Nomes1.replace('&', '&').replace('+', '+').replace('/.png', ' ').replace('*','*').lower())
            #Nomes = unicodedata.normalize('NFC', unicode(name, 'utf_8')).replace('&', '&amp;').lower())

            newPiconName = newName1  # PARA .services-todos2.sh
            #newPiconName = newName2 + ".br"  # PARA .services-todos2.sh
            # newPiconName = newName2  + "."
            if int(ref[4]) < 26:  # service type in decimal
                if (len(newName2) and newPiconName in paths) or oldPiconName in paths or oldPiconName2 in paths:
                    # found = True
                    finished = True
                else:

                    messages.append((Nomes1, newPiconName, oldPiconName2, Nomes3, sat, int(ref[4]))) # P/ message[0] message[1] message[2]....
                i += 1
                if i % 100 == 0:
                    # self["statustext"].text = _("LENDO CANAIS ENCONTRADOS...") # OK
                    print "Lendo %i Canais... Encontrados " % (i)
                    # self["status"].setText(_("Lendo canais encontrados..."))
                    # if i == 500:
                #	break

                serviceTypes.append(int(ref[4]))

                # sortOrder = messages.sort(key=lambda x: (re.split(":",x[1]))[2] ,reverse=False)
                # messages = sortByValueRecursive(messages, sortOrder)
        messages = (messages)

        i = 0
        #log = ''
        log1 = ''
        for message in messages:
            if i % 25 == 0:
                log1 += ''
                # log += '%s \n' % (message[2])
                # log += 'touch %s > %spng \n' % (message[2],message[2])
            #log += "touch %s > /usr/share/enigma2/picon/%spng\n" % (message[2], message[2])  # touch 1_0_19_1D8_3D_1_B54B098_0_0_0. > 1_0_19_1D8_3D_1_B54B098_0_0_0.png
            ##log += '"%s","%s","%s","%s", %i\n' % (message[0],message[1],message[2], satname(message[3]), message[4])
            # log1 += 'mv /tmp/nomes/%s /usr/share/enigma2/picon/%spng \n' % (message[1],message[2])
            # log1 += "cp /tmp/nomes/%s /usr/share/enigma2/picon/%spng &> /dev/null\n"%(message[1],message[2])
            log1 += '\t\t<channel id="%s">%s:</channel> <!-- %s - %s -->\n' % (message[0], message[2], message[3], message[4])
            i += 1

        arquivo.write(log1)   # PARA .services-todos2.sh
        #zf.writestr(outlog2 + '-todos2' + logExt, log1.line.replace("#NULO", ""))  # PARA .services-todos2.sh
        #zf.write(log1.replace("cp /tmp/nomes/.png /usr/share/enigma2/picon/", "#NULO"))  # PARA .services-todos2.sh

        arquivo.close()
        if __name__ == '__main__':
            print('SOURCE GERADO ARQUIVO > /etc/enigma2/channels.xml.gz')
            # self["status"].setText(_("me executou pelo terminal"))
        else:
            #print('me executou como um modulo')
            #self["status"].setText(_("me executou como um modulo"))

            if not os.path.isfile("/tmp/nomes") and not os.path.isdir("/tmp/nomes"):
                os.mkdir("/tmp/nomes")
        os.system("ls &> /dev/null")
        finished = True

        print "FINALIZANDO..."

        LER1 = canaisxml
        GERADO = '/tmp/.canais2.xml'
        GRAVAR1 = open(LER1, "r+w")
        GRAVAR1.close()
        LER = LER1
        REMOVER = ['<channel id="">', 'Teste', 'Radio', 'Anos', 'Hab', 'Classica', 'Blues', 'Sertanejo', 'Festa Junina',
                   'Jazz', 'Bossa Nova', 'New Rock', 'Romanticas', 'Trilhas Sonoras', 'Lounge', 'Gospel', 'Forro',
                   'Teletema', 'Samba', 'POP Hits', 'Hip Hop', 'Pop Hits', 'Eletronica', 'Reggae', 'Rock Brasil',
                   'Roberto Carlos', 'ISDB-T', 'Banda C','Soft Hits','Funk e Rap','BH FM', 'TVEXEC', 'TVTEC', 'Metal', 'MPB', 'PVR','Festa', 'Rock Classico','Classica','Pagode', 'Musica', 'Divas', 'Soft hits', 'FM Express', 'CBN SP', 'Band News FM', 'Nativa FM', 'Band FM', 'Michael Jackson', '1SEG', 'Madonna', '"Disco"',
                   '"Kids"','>1:0:2:']  # REMOVE LINHAS QUE CONTEM... "1:0:2:" --> RÁDIOS
        with open(LER) as oldfile, open(GERADO, 'w+') as newfile:
            for line in oldfile:
                if not any(bad_word in line for bad_word in REMOVER):
                    # newfile.write("")
                    newfile.write(line
						.replace('2429', '(117w-C)')
						.replace('2469', '(113w-C)')
						.replace('2710', '(89-ku)')
						.replace('2760', '(84w-C)')
						.replace('2849', '(75w-C)')
						.replace('2899', '(70w-C)')
						.replace('2900', '(CLARO DTH)')
						.replace('Mudar n�mero', '(Planejada - 65w-C)')
						.replace('2949', '(65w-C)')
						.replace('Mudar n�mero 2','( Planejada - 61w-C)')
						.replace('2989','(61w-C)')
						.replace('2990', '(VIVO AMAZONAS)')
						.replace('3019', '(58w-C)')
						.replace('3044', '(55.5w-C)')
						.replace('3124', '(47.5w-C)')
						.replace('3149', '(45w-C)')
						.replace('3168', '(43w-C)')
						.replace('3169', '(SKY HDTV)')
						.replace('3193','(Planejada - 40.5w-C)')
						.replace('3194','(40.5w-C)')
						.replace('3224', '(37.5w-C)')
						.replace('3254', '(34.5w-C)')
						.replace('3379','(22w-C)')
						.replace('3419','(18w-C)')
						.replace('3459', '(14w-C)')
						.replace('3489', '(11w-C)')
						.replace('3519', '(8w-C)')
						.replace('3569', '(3w-C)')
						.replace('3570', '(3w-ku)')
						.replace('65535', 'NET TV')
						.replace('61166', '(ISDB-T)')
						.replace(' ">', '">'))
                # newfile.write(line.replace('2990','61w-ku').replace('2850', '70w-C').replace('2900','70w-ku'))
                # GRAVAR.write("")
                # os.system("rm /ch-refe.xml && rm /ch-todos.xml &> /dev/null")

        #os.system("rm /etc/enigma2/canais.xml.gz &> /dev/null")
        #os.system("rm /tmp/.services.zip && rm /tmp/ch-refe.xml && gzip -c /etc/enigma2/canais.xml >/etc/enigma2/canais.xml.gz &> /dev/null")
        from datetime import datetime
        datahoje = datetime.now().strftime('Gerado em %d/%m/%Y  %H:%M:%S')
        LERCABE = '/tmp/.cabecalho.xml'
        CABECA1 = open(LERCABE,"w+") # SEMPRE CRIA UM NOVO ARQUIVO
        CABECA1.write('<?xml version="1.0" encoding="latin-1"?>\n\t<!-- %s -->\n\t<channels>\n' % datahoje)
        CABECA1.close()
        filenames = ['/tmp/.cabecalho.xml', '/tmp/.canais2.xml'] # UNIR ARQUIVOS
        os.system("rm /etc/enigma2/channels.xml.gz &> /dev/null")
        os.system("rm /etc/enigma2/channels.xml &> /dev/null")
        with open('/tmp/channels.xml', 'w+') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

        SAIDA  = '/tmp/channels.xml'
        GRAVAR = open(SAIDA, "a+") # ESCREVE NO FINAL DO ARQUIVO
        GRAVAR.write('\t</channels>')
        GRAVAR.close()
#os.system("chmod 777 /tmp/canais.xml &> /dev/null")
#os.system("gzip -c /tmp/canais.xml")
#os.system("gzip -c /etc/enigma2/canais.xml >/etc/enigma2/canais.xml.gz &> /dev/null")
        #os.system("rm /tmp/.cabecalho.xml && rm /tmp/.canais2.xml &> /dev/null")
	os.system("cp /tmp/channels.xml /etc/enigma2/ &> /dev/null")
	os.system("gzip -k /etc/enigma2/channels.xml &> /dev/null")
	print "OK"

def slotName(namespace):
    slot = slot1(namespace)
    return satname(slot)

def satname(slot):
    if slot == 65535:
        return 'cable'
    elif slot == 61166:
        return 'terrestrial'
    while slot < -1800:
        slot += 3600
    while slot > 1800:
        slot -= 3600
        westeast = 'E' if slot >= 0 else 'W'
    return str(round(float(abs(slot)) / 10, 1)) + westeast


def slot1(namespace):
    return int(namespace[:len(namespace) - 4], 16)
if __name__ == '__main__':
    main()


### FIM
