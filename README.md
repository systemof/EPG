# `EPG System - Guia de Programação` 

O **EPG System** é uma ferramenta essencial para dispositivos compatíveis com **Enigma2**, fornecendo guias de programação detalhados para os canais favoritos dos usuários. Este projeto inclui arquivos com informações sobre a programação e IDs dos canais, além de scripts para instalação de plugins, facilitando a configuração e atualização do EPG em seu dispositivo.

---

## 🟢 Introdução

O sistema EPG (Electronic Program Guide) é uma ferramenta essencial para dispositivos Enigma2, permitindo que você tenha acesso a guias de programação detalhados para seus canais favoritos. Este projeto oferece arquivos e scripts para facilitar a configuração e atualização do EPG em seu dispositivo.

---

## 🟢 Atualizações Recentes

- **[25/03/2023]** Adicionados canais Paramount+
- **[25/03/2023]** Adicionados canais Nosso Futebol 1 e 2
- **[23/02/2024]** Adicionados ESPN5, ESPN6, AdultSwim, DW Espanhol e outros.
- **[20/12/2024]** Adicionado Mezzo, Uol Tv, Times | Exclusivo CNBC, Universal Premiere e Reality, Markket
---

## 🟢 Arquivos Importantes

### 1. `guide.xml.gz`
- Contém a programação completa dos canais.  
- **É necessário descompactar este arquivo antes de usá-lo.** O arquivo descompactado será o `guide.xml`.
- As IDs no `guide.xml.gz` devem coincidir com as do `channels ids.xml`.

### 2. `channel id.xml`
- Contém as IDs dos canais no formato correto.

### 3. `channels ids.xml`
- IDs dos canais utilizados para sincronização no `guide.xml.gz`.

---

## 🟢 Como usar o Guide.xml

O arquivo `guide.xml` é responsável por fornecer a programação dos canais para o seu dispositivo Enigma2. Siga as etapas abaixo para configurá-lo corretamente:

### 🟢 1. Transferindo o Arquivo para o Dispositivo
- No plugin Powerlame, escolha a opção **"Baixar source para EPGimport"**.
- O Powerlame irá baixar o arquivo `guide.xml.gz` e descompactá-lo no local correto para o EPG Importer.

### 🟢 2. Configurando o EPG Importer
- No menu do dispositivo, acesse `**Configurações > Plugins > EPG Importer**`.
- Dentro do EPG Importer:
  - Verifique se o local do arquivo `guide.xml` está configurado corretamente. O local padrão é `/etc/enigma2/`.
  - Ative a opção para importar o guia automaticamente ou manualmente.

### 🟢 3. Executando a Importação
- Após configurar o arquivo, selecione a opção **"Importar Agora"** no EPG Importer.
- O dispositivo processará o arquivo e atualizará o guia de programação dos canais.

### 🟢 4. Verificando a Programação
- Após a importação, volte à interface principal do dispositivo.
- Navegue pelos canais para verificar se a programação está aparecendo corretamente.

### 🟢 Dica:
Certifique-se de que o arquivo `guide.xml` está atualizado e que os IDs dos canais no arquivo correspondem aos IDs no dispositivo.

---

## 🟢 Solução de Problemas

- **A programação não aparece:** Verifique se as IDs no `guide.xml` correspondem às do dispositivo. Certifique-se também de que o arquivo foi importado corretamente.
- **Erro ao importar:** Confirme que o arquivo foi colocado no diretório correto e que possui as permissões adequadas. Verifique também a conexão com a internet.
- **EPG desatualizado:** Certifique-se de baixar a versão mais recente do `guide.xml`. Se o problema persistir, tente reimportar o arquivo.

---

## 🟢 Pré-requisitos

Para usar este sistema, você precisa de:

- Dispositivo compatível com **Enigma2**
- Acesso ao terminal do dispositivo
- Conexão com a internet

---

## 🟢 Instalando o `Powerlame`

O plugin **Powerlame** é essencial para gerenciar e importar o EPG no seu dispositivo Enigma2. Para instalá-lo, siga os passos abaixo:

1. Abra o terminal do seu dispositivo.
2. Execute o comando abaixo para baixar e instalar o plugin:
   ```bash
   wget -qO- --no-check-certificate "https://raw.githubusercontent.com/systemof/EPG/master/powerlame.sh" | sed 's///' | bash
   ```

     ```bash
   wget -qO- --no-check-certificate "https://raw.githubusercontent.com/systemof/EPG/master/powerlame.sh" | bash

   ```
3. Após a instalação, o plugin estará disponível no menu de plugins do seu dispositivo.

### 🟢 Explicação do Comando
- `wget -qO-`: Baixa o script e exibe o conteúdo.
- `sed 's/\r//'`: Remove caracteres indesejados.
- `bash`: Executa o script diretamente.

---

## 🟢 Bot para monitorar oscam (notfound , timeout)


   ```# ✅ Monitoramento de ECM com Alerta via Telegram (Enigma2 / ATTO)

Este guia cobre todo o processo de criação, configuração e ativação de um sistema de alerta automático via Telegram para falhas de ECM no OSCam.

---

## 🧾 1. Criar o Bot do Telegram

1. No Telegram, busque por `@BotFather`
2. Digite `/newbot`
3. Dê um nome e um username para o bot
4. Ao final, será fornecido um **Token** no formato:
   ```
   123456789:AA...SeuTokenAqui...
   ```
5. Copie esse token — será usado no script.

---

## 🧾 2. Obter o Chat ID

1. No navegador, acesse:
   ```
   https://api.telegram.org/bot<SEU_TOKEN>/getUpdates
   ```
2. Envie uma mensagem para o bot.
3. Recarregue o link acima.
4. Copie o valor de `"chat":{"id":...}` → esse é o `CHAT_ID`.

---

## 🧾 3. Configurar OSCam para gerar log

1. Edite o arquivo `oscam.conf`
2. Adicione (ou edite) a seção `[global]`:
   ```ini
   [global]
   logfile = /var/log/oscam.log
   ```

3. Reinicie o OSCam:
   ```bash
   killall oscam
   sleep 2
   /usr/bin/oscam -c /etc/tuxbox/config &
   ```

---

## 🧾 4. Instalar os scripts de alerta

### Coloque os dois arquivos no diretório:
```
/etc/oscam/
```

### Torne-os executáveis:
```bash
chmod +x /etc/oscam/ecm_alerta_telegram.sh
chmod +x /etc/oscam/ecm_alerta_loop.sh
```

---

## 🧾 5. Scripts

### `ecm_alerta_telegram.sh`:
- Lê as últimas 2000 linhas do log `/var/log/oscam.log`
- Detecta repetições de `timeout` ou `not found`
- Envia alerta via Telegram
- Evita alertas duplicados

### `ecm_alerta_loop.sh`:
- Executa o script de alerta a cada 60 segundos (loop infinito)

---

## 🧾 6. Executar o script em background (teste manual)

```bash
/etc/oscam/ecm_alerta_loop.sh &
```

---

## 🧾 7. Rodar o alerta automaticamente no boot

1. Edite `/etc/rc.local`
2. Antes do `exit 0`, adicione:
   ```bash
   /etc/oscam/ecm_alerta_loop.sh &
   ```

3. Torne o `rc.local` executável:
   ```bash
   chmod +x /etc/rc.local
   ```

---

## 🧾 8. Verificar funcionamento

- Você deverá receber uma mensagem no Telegram com a ECM com erro.
- Pode testar com:
   ```bash
   echo "ECM FAKE TEST 1802@DEADBEEF timeout (4000 ms)" >> /var/log/oscam.log
   bash /etc/oscam/ecm_alerta_telegram.sh
   ```

---

✅ Pronto! Agora o seu ATTO (ou STB com Enigma2) irá alertar você sempre que houver falha grave de ECM no OSCam.

   ```


## 🟢 Exemplo de Interface do `Powerlame` 

![Exemplo de Powerlame](https://imgur.com/R2QGriA.png)

---

## Exemplo de Arquivo `guide.xml`

```xml
<channel id="ESPN5">
    <display-name>ESPN 5</display-name>
</channel>
<programme start="20240323080000 +0000" stop="20240323090000 +0000" channel="ESPN5">
    <title>Jogo ao Vivo</title>
    <desc>Transmissão do jogo ao vivo.</desc>
</programme>
```

---

## 🟢 Perguntas Frequentes (FAQ)

<details>
<summary>1. O que é o EPG System?</summary>
O **EPG System** é uma solução para gerenciar guias de programação de TV (EPG) em dispositivos compatíveis com **Enigma2**. Ele permite visualizar a programação dos canais diretamente no seu aparelho.
</details>

<details>
<summary>2. Como faço para instalar o plugin Powerlame?</summary>
Você pode instalar o plugin Powerlame seguindo os passos na seção [Instalando o Powerlame](#instalando-o-powerlame). O comando principal é:
```bash
wget -qO- --no-check-certificate "https://raw.githubusercontent.com/systemof/EPG/master/powerlame.sh" | sed 's/
//' | bash
```
</details>

<details>
<summary>3. Meu guia não está carregando, o que devo fazer?</summary>
Certifique-se de que:
- O arquivo `guide.xml` foi transferido corretamente para o diretório `/etc/enigma2/` do seu dispositivo.
- As IDs dos canais no arquivo correspondem às IDs configuradas no aparelho.
- O dispositivo tem conexão com a internet.

Se o problema persistir, tente reimportar o guia no menu do plugin **EPG Importer**.
</details>

<details>
<summary>4. Preciso de internet para usar o EPG System?</summary>
Sim, a internet é necessária para baixar e atualizar o arquivo `guide.xml`. Após a atualização, o guia pode ser usado offline.
</details>

<details>
<summary>5. Como faço para atualizar a programação?</summary>
Baixe o arquivo mais recente do `guide.xml.gz` e siga os passos descritos na seção [Como usar o Guide.xml](#como-usar-o-guidexml).
</details>

---

## 🟢 Contribuições

Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou relatar problemas, siga os passos abaixo:

1. Abra uma **issue** para discutir as mudanças propostas.
2. Faça um **fork** do repositório e implemente as mudanças.
3. Envie um **pull request** com suas alterações.

Certifique-se de seguir as diretrizes de estilo e padrões de codificação do projeto.

---

[![Build Status](https://img.shields.io/travis/systemof/EPG.svg)](https://travis-ci.org/systemof/EPG)

---

## Licença
Livre








































    

























































    
















# `EPG System - Guia de Programação` 

O **EPG System** é uma ferramenta essencial para dispositivos compatíveis com **Enigma2**, fornecendo guias de programação detalhados para os canais favoritos dos usuários. Este projeto inclui arquivos com informações sobre a programação e IDs dos canais, além de scripts para instalação de plugins, facilitando a configuração e atualização do EPG em seu dispositivo.

---

## 🟢 Introdução

O sistema EPG (Electronic Program Guide) é uma ferramenta essencial para dispositivos Enigma2, permitindo que você tenha acesso a guias de programação detalhados para seus canais favoritos. Este projeto oferece arquivos e scripts para facilitar a configuração e atualização do EPG em seu dispositivo.

---

## 🟢 Atualizações Recentes

- **[25/03/2023]** Adicionados canais Paramount+
- **[25/03/2023]** Adicionados canais Nosso Futebol 1 e 2
- **[23/02/2024]** Adicionados ESPN5, ESPN6, AdultSwim, DW Espanhol e outros.
- **[20/12/2024]** Adicionado Mezzo, Uol Tv, Times | Exclusivo CNBC, Universal Premiere e Reality, Markket
---

## 🟢 Arquivos Importantes

### 1. `guide.xml.gz`
- Contém a programação completa dos canais.  
- **É necessário descompactar este arquivo antes de usá-lo.** O arquivo descompactado será o `guide.xml`.
- As IDs no `guide.xml.gz` devem coincidir com as do `channels ids.xml`.

### 2. `channel id.xml`
- Contém as IDs dos canais no formato correto.

### 3. `channels ids.xml`
- IDs dos canais utilizados para sincronização no `guide.xml.gz`.

---

## 🟢 Como usar o Guide.xml

O arquivo `guide.xml` é responsável por fornecer a programação dos canais para o seu dispositivo Enigma2. Siga as etapas abaixo para configurá-lo corretamente:

### 🟢 1. Transferindo o Arquivo para o Dispositivo
- No plugin Powerlame, escolha a opção **"Baixar source para EPGimport"**.
- O Powerlame irá baixar o arquivo `guide.xml.gz` e descompactá-lo no local correto para o EPG Importer.

### 🟢 2. Configurando o EPG Importer
- No menu do dispositivo, acesse `**Configurações > Plugins > EPG Importer**`.
- Dentro do EPG Importer:
  - Verifique se o local do arquivo `guide.xml` está configurado corretamente. O local padrão é `/etc/enigma2/`.
  - Ative a opção para importar o guia automaticamente ou manualmente.

### 🟢 3. Executando a Importação
- Após configurar o arquivo, selecione a opção **"Importar Agora"** no EPG Importer.
- O dispositivo processará o arquivo e atualizará o guia de programação dos canais.

### 🟢 4. Verificando a Programação
- Após a importação, volte à interface principal do dispositivo.
- Navegue pelos canais para verificar se a programação está aparecendo corretamente.

### 🟢 Dica:
Certifique-se de que o arquivo `guide.xml` está atualizado e que os IDs dos canais no arquivo correspondem aos IDs no dispositivo.

---

## 🟢 Solução de Problemas

- **A programação não aparece:** Verifique se as IDs no `guide.xml` correspondem às do dispositivo. Certifique-se também de que o arquivo foi importado corretamente.
- **Erro ao importar:** Confirme que o arquivo foi colocado no diretório correto e que possui as permissões adequadas. Verifique também a conexão com a internet.
- **EPG desatualizado:** Certifique-se de baixar a versão mais recente do `guide.xml`. Se o problema persistir, tente reimportar o arquivo.

---

## 🟢 Pré-requisitos

Para usar este sistema, você precisa de:

- Dispositivo compatível com **Enigma2**
- Acesso ao terminal do dispositivo
- Conexão com a internet

---

## 🟢 Instalando o `Powerlame`

O plugin **Powerlame** é essencial para gerenciar e importar o EPG no seu dispositivo Enigma2. Para instalá-lo, siga os passos abaixo:

1. Abra o terminal do seu dispositivo.
2. Execute o comando abaixo para baixar e instalar o plugin:
   ```bash
   wget -qO- --no-check-certificate "https://raw.githubusercontent.com/systemof/EPG/master/powerlame.sh" | sed 's///' | bash
   ```
3. Após a instalação, o plugin estará disponível no menu de plugins do seu dispositivo.

### 🟢 Explicação do Comando
- `wget -qO-`: Baixa o script e exibe o conteúdo.
- `sed 's/\r//'`: Remove caracteres indesejados.
- `bash`: Executa o script diretamente.

---

## 🟢 Exemplo de Interface do `Powerlame` 

![Exemplo de Powerlame](https://imgur.com/R2QGriA.png)

---

## Exemplo de Arquivo `guide.xml`

```xml
<channel id="ESPN5">
    <display-name>ESPN 5</display-name>
</channel>
<programme start="20240323080000 +0000" stop="20240323090000 +0000" channel="ESPN5">
    <title>Jogo ao Vivo</title>
    <desc>Transmissão do jogo ao vivo.</desc>
</programme>
```

---

## 🟢 Perguntas Frequentes (FAQ)

<details>
<summary>1. O que é o EPG System?</summary>
O **EPG System** é uma solução para gerenciar guias de programação de TV (EPG) em dispositivos compatíveis com **Enigma2**. Ele permite visualizar a programação dos canais diretamente no seu aparelho.
</details>

<details>
<summary>2. Como faço para instalar o plugin Powerlame?</summary>
Você pode instalar o plugin Powerlame seguindo os passos na seção [Instalando o Powerlame](#instalando-o-powerlame). O comando principal é:
```bash
wget -qO- --no-check-certificate "https://raw.githubusercontent.com/systemof/EPG/master/powerlame.sh" | sed 's/
//' | bash
```
</details>

<details>
<summary>3. Meu guia não está carregando, o que devo fazer?</summary>
Certifique-se de que:
- O arquivo `guide.xml` foi transferido corretamente para o diretório `/etc/enigma2/` do seu dispositivo.
- As IDs dos canais no arquivo correspondem às IDs configuradas no aparelho.
- O dispositivo tem conexão com a internet.

Se o problema persistir, tente reimportar o guia no menu do plugin **EPG Importer**.
</details>

<details>
<summary>4. Preciso de internet para usar o EPG System?</summary>
Sim, a internet é necessária para baixar e atualizar o arquivo `guide.xml`. Após a atualização, o guia pode ser usado offline.
</details>

<details>
<summary>5. Como faço para atualizar a programação?</summary>
Baixe o arquivo mais recente do `guide.xml.gz` e siga os passos descritos na seção [Como usar o Guide.xml](#como-usar-o-guidexml).
</details>

---

## 🟢 Contribuições

Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou relatar problemas, siga os passos abaixo:

1. Abra uma **issue** para discutir as mudanças propostas.
2. Faça um **fork** do repositório e implemente as mudanças.
3. Envie um **pull request** com suas alterações.

Certifique-se de seguir as diretrizes de estilo e padrões de codificação do projeto.

---

[![Build Status](https://img.shields.io/travis/systemof/EPG.svg)](https://travis-ci.org/systemof/EPG)

---

## Licença
Livre








































    

























































    
















