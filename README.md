# EPG System - Guia de Programação

Este projeto fornece guias de programação de canais para dispositivos compatíveis com o **Enigma2**. Ele inclui arquivos com informações sobre a programação e IDs dos canais, além de scripts para instalação de plugins.

## Atualizações Recentes

- **[25/03/2023]** Adicionados canais Paramount+
- **[25/03/2023]** Adicionados canais Nosso Futebol 1 e 2
- **[23/02/2024]** Adicionados ESPN5, ESPN6, AdultSwim, DW Espanhol e outros.

## Arquivos Importantes

### 1. `guide.xml.gz`
- Contém a programação completa dos canais em formato XML comprimido.
- **É necessário descompactar este arquivo antes de usá-lo.** O arquivo descompactado será o `guide.xml`
- As IDs no `guide.xml` devem coincidir com as do `channels ids.xml` para que a programação seja exibida corretamente.

### 2. `channel id.xml`
- Contém as IDs dos canais no formato correto. Este arquivo será utilizado pelo plugin Powerlame.

### 3. `channels ids.xml`
- Contém as IDs dos canais utilizados para sincronização com o `guide.xml`. Exemplo:
  ```xml
  <channel id="ESPN5">
    <channel-id>12345</channel-id>
  </channel>
  
  Como usar o guide.xml

O arquivo guide.xml é responsável por fornecer a programação dos canais para o seu dispositivo Enigma2. Siga as etapas abaixo para configurá-lo corretamente:
1. Transferindo o Arquivo para o Dispositivo

    No plugin Powerlame, escolha a opção "Baixar source para EPGimport". O Powerlame irá baixar o arquivo guide.xml.gz e descompactá-lo no local correto para o EPG Importer.

2. Configurando o EPG Importer

    No menu do dispositivo, acesse Configurações > Plugins > EPG Importer.

    Dentro do EPG Importer:

        Verifique se o local do arquivo guide.xml está configurado corretamente. O local padrão é /etc/enigma2/.

        Ative a opção para importar o guia automaticamente ou manualmente, conforme sua preferência.

3. Executando a Importação

    Após configurar o arquivo, selecione a opção "Importar Agora" no EPG Importer.

    O dispositivo processará o arquivo e atualizará o guia de programação dos canais.

4. Verificando a Programação

    Após a importação, volte à interface principal do dispositivo.

    Navegue pelos canais para verificar se a programação está aparecendo corretamente.

Dica:

Certifique-se de que o arquivo guide.xml está atualizado e que os IDs dos canais no arquivo correspondem aos IDs no dispositivo.
Solução de Problemas

    A programação não aparece:

        Verifique se as IDs no guide.xml correspondem às do channels ids.xml do dispositivo.

        Certifique-se de que o arquivo guide.xml foi descompactado corretamente (se aplicável).

    Erro ao importar:

        Confirme que o arquivo foi colocado no diretório correto do dispositivo e que possui as permissões de leitura adequadas.

        Verifique se o arquivo guide.xml está bem formatado, sem erros de sintaxe XML.

        Consulte os logs do seu dispositivo Enigma2 para identificar erros específicos.

    EPG desatualizado: Certifique-se de baixar a versão mais recente do guide.xml.

Pré-requisitos

Para usar este sistema, você precisa de:

    Dispositivo compatível com Enigma2

    Acesso ao terminal do dispositivo (para instalar o Powerlame, caso necessário)

    Conexão com a internet

Instalando o Powerlame

O Powerlame é um plugin que facilita a importação do guide.xml para o EPG Importer, além de permitir baixar outros sources de EPG. Para instalar o plugin Powerlame no seu dispositivo Enigma2, execute o comando abaixo no terminal:

      
wget -qO- --no-check-certificate "https://raw.githubusercontent.com/systemof/EPG/master/powerlame.sh" | sed 's/\r//' | bash

    Explicação do Comando

    wget -qO-: Baixa o script e exibe o conteúdo.

    sed 's/\r//': Remove caracteres indesejados.

    bash: Executa o script diretamente.

Exemplo de Interface do Powerlame

![alt text](https://imgur.com/R2QGriA.png)


Este é um exemplo de interface do plugin Powerlame, a interface pode variar dependendo da versão.
Exemplo de Arquivo guide.xml

      
<channel id="ESPN5">
    <display-name>ESPN 5</display-name>
</channel>
<programme start="20240323080000 +0000" stop="20240323090000 +0000" channel="ESPN5">
    <title>Jogo ao Vivo</title>
    <desc>Transmissão do jogo ao vivo.</desc>
</programme>Imagens

Substitua a imagem abaixo pelo conteúdo real que mostra a interface do guia de programação no dispositivo Enigma2.

![alt text](https://imgur.com/hdsaskI.png)

Contribuições

Contribuições são bem-vindas! Para enviar melhorias ou relatar problemas, abra uma issue ou pull request no repositório [link do repositório aqui]. Se precisar de suporte, entre em contato pelo [link do fórum ou suporte aqui].

    
















