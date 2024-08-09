**Informações:** 
-----------------------------

<details>
<summary><b>Atualizaçoes do EPG systemof</b></summary>

* [25/03/2023] Adicionado canais Paramount+
* [25/03/2023]  Adicionado canal Nosso Futebol 1 e 2
* [23/02/2024]  Adicionado ESPN5 e 6 - AdultSwin - DW Espanhol e +

</details>

<details>
<summary><b>Instruções lamedbtochannels</b></summary>

* Gerar channels.xml.gz (somente imagens com python2)
* Baixe o script lamedbtochannels.py e coloque-o na pasta /etc/enigma2/
* No terminal Linux ou Putty navegue até a pasta enigma2
* login as:root
* cd /etc/enigma2
* Para ser possível executá-lo: chmod +x lamedbtochannels.py
* Após, para executar e criar o channels:python lamedbtochannels.py
* O arquivo criará um arquivo chamado channels.xml e um channels.xml.gz na pasta /etc/enigma2.
* Caso não queira o channels.xml, é só colocar a linha do comando em si como comentário (#).
* Em imagens com python3 não funciona(turing versão 7 acima),se for usar no turing instale o powerlamaneturing que se
encontra nesse repositorio para  gerar o channels.xml.gz.</details>

<details>
<summary><b>Instruções lamedbtochannels para python 3 (imagens 7.0 em diante)</b></summary>

* Creditos fc_candido | sam564 (somente imagens com python3)
* Gerar channels.xml.gz (somente imagens com python3)
* Baixe o script lamedbtochannels.py e coloque-o na pasta /etc/enigma2/
* No terminal Linux ou Putty navegue até a pasta enigma2
* login as:root
* cd /etc/enigma2
* Para ser possível executá-lo: chmod +x lamedbtochannels.py
* Após, para executar e criar o channels:python lamedbtochannels.py
* O arquivo criará um arquivo chamado channels.xml e um channels.xml.gz na pasta /etc/enigma2.
* Caso não queira o channels.xml, é só colocar a linha do comando em si como comentário (#).
* Essa versão só funciona em imagens python 3 ex: Turing a partir da versão 7




</details>
<details>

<summary><b>guide.xml.gz</b></summary>

* Guia com a programação dos canais
* As ids do guia e do channels devem ser identicas.

<img src="https://imgur.com/hdsaskI.png">


</details>

<details>

<summary><b>channel id.xml</b></summary>

* Id dos canais 

</details>

<details>
<summary><b>channels ids.xml</b></summary>

* Id dos canais no formato usado no guide.xml

</details>

<details>
<summary><b>powerlame</b></summary>

* Plugin para gerar favoritos(localmente)
* Source do EPG
* Picons
* Corrigido bug que travava o aparelho ao gerar favoritos localmente (06/08/2024)

</details>
<details>
<summary><b>Picons para  Turing</b></summary>

* Pasta com picons para turing (SP)
* Adicionado canais Nosso Futebol (12/03/24)
* Adicionado canais Paramount+ (13/03/24)
* Adicionado canais ESPN 5 e 6 - (13/03/24)
* Adicionado canais DWespanhol-USA-AdultSwin-TNTNovelas-NSports (13/03/24)

	
</details>
<details>
<summary><b>Easy Channels (Atto Turing e Atto Plus)</b></summary>

* (Gera o channels.xml.gz)
* Escolha a versão correta para o seu aparelho


	
</details>
</details>
<details>
<summary><b>Picon Downloader</b></summary>

* Gera os picons para Atto Turing, pixel plus use o powerlame


	
</details>








