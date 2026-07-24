#!/bin/sh

validate_ipk() {
  f="$1"
  # Needs to be larger than 50KB and an ar archive
  if [ ! -s "$f" ]; then
    echo "ERRO: arquivo $f não existe ou está vazio." >&2
    return 1
  fi
  sz=$(wc -c < "$f" 2>/dev/null || echo 0)
  if [ "$sz" -lt 51200 ]; then
    echo "ERRO: arquivo $f muito pequeno ($sz bytes). Download pode ter falhado." >&2
    return 1
  fi
  if command -v ar >/dev/null 2>&1; then
    if ! ar t "$f" >/dev/null 2>&1; then
      echo "ERRO: $f não é um pacote .ipk válido." >&2
      return 1
    fi
  fi
  return 0
}

# Definir o URL do pacote .ipk
IPK_URL="https://api.github.com/repos/systemof/EPG/contents/enigma2-plugin-extensions-powerlamerev_8.7_all.ipk?ref=master"

# Baixar o pacote .ipk
echo "Baixando o plugin do URL: $IPK_URL"
wget -O /tmp/enigma2-plugin-extensions-powerlamerev_8.7_all.ipk "$IPK_URL"

# Verificar se o download foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Download concluído com sucesso."

    # Instalar o pacote .ipk
    echo "Instalando o plugin..."
    validate_ipk "/tmp/enigma2-plugin-extensions-powerlamerev_8.7_all.ipk" && opkg install /tmp/enigma2-plugin-extensions-powerlamerev_8.7_all.ipk

    # Verificar se a instalação foi bem-sucedida
    if [ $? -eq 0 ]; then
        echo "Plugin instalado com sucesso."

        # Remover o arquivo .ipk baixado
        rm -f /tmp/enigma2-plugin-extensions-powerlamerev_8.7_all.ipk
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
