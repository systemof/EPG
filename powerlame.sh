#!/bin/sh

# Definir o URL do pacote .ipk
IPK_URL="https://github.com/systemof/EPG/raw/master/enigma2-plugin-extensions-powerlamerev_8.6_all.ipk"

# Baixar o pacote .ipk
echo "Baixando o plugin do URL: $IPK_URL"
wget -O /tmp/enigma2-plugin-extensions-powerlamerev_8.6_all.ipk "$IPK_URL"

# Verificar se o download foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Download concluído com sucesso."

    # Instalar o pacote .ipk
    echo "Instalando o plugin..."
    opkg install /tmp/enigma2-plugin-extensions-powerlamerev_8.6_all.ipk

    # Verificar se a instalação foi bem-sucedida
    if [ $? -eq 0 ]; then
        echo "Plugin instalado com sucesso."

        # Remover o arquivo .ipk baixado
        rm -f /tmp/enigma2-plugin-extensions-powerlamerev_8.6_all.ipk
        echo "Arquivo temporário removido."

        # Reiniciar o Enigma2
        echo "Reiniciando o Enigma2..."
        reboot
    else
        echo "Erro na instalação do plugin."
    fi
else
    echo "Erro ao baixar o plugin."
fi
