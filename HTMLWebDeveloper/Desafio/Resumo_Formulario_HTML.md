### Resumo Formulário HTML

#### Tag **&lt;form>**
#####Propriedade desta tag:
* **action** serve para dizer pra onde vão as informações do formulário.

* **name** vai ser utilizada no javascript para encontrar e capturar os elementos deste formulário.

* **method**, com duas opções **GET** ou **POST**.
  * GET não é seguro envia as informações por url;
  * POST envia as informações por requisição ao servidor.
* **target** para poder configurar do envio do formulário ser feito em outra página com valor _blanck.
* **autocomplete** com duas possibilidades, **on** ou **off**.
  * **on** - se optado por este atributo o navegador irá armazenar os dados e na próxima entrada no mesmo formulário os campos virão pré-preenchidos.
  * **off** - desabilida os dados pré-preenchidos.
* **onsubmit** - tudo que tiver on no html trata de um **evento** javascript, no caso do onsubmit a utilização vai ser para quando clicar no botão enviar, que evento será chamado.

#### Input
* **Alguns Tipos de Input**
  * **text** - para inserção de texto comum.
  * **number** - para inserção de números, com algumas propriedades:
    * min: menor número aceito.
    * max: maior número aceito.
    * step: pular de tanto em tanto.
  * **button** - usar a tag button normal.
  * **range** - barra de progrresso, com propriedade:
    * min;
    * max;
  * **color** - cria uma caixa de seleção de cor;
  * **e-mail** - cria campo de e-mail obrigando preenchimento com @;
  * **url** - campo próprio para inserção de url, com restrição de preenchimento.
  * **date** - abre um calendário conforme navegador;
  * **week** - calendário de semana;
  * **month** - calendário de mês;
  * **checkbox** - cria caixa de seleção, com seleção de vários ao mesmo tempo, abaixo as propiedades principais;
    * name - esta inforamção serve para agrupar os check, como ele aceita vários checkbox com mesmo **name**, então é enviado para o servidor o **'name'**=**'value'**, sendo vário valores, será necessário transformar esse name em uma lista para receber vários valores, basta colocar os colchetes após o nome, desta forma: **name=nomeexemplo[ ]**
    * disabled - deixa o checkbox aparente, mas desabilitado para marcação.
  * **radio** - caixa de seleção, mas ao contrário do checkbox apenas uma opção pode ser selecionado, as caixas para funcionarem deverão ter o mesmo **name** para agrupar e funcionar a marcação apenas no item desejado;
  * **file** - campo para anexar um arquivo.
    * multiple - para escolher vários arquivos, se não atribuir esta propriedade o padrão é poder escolher apenas um arquivo.
  * **hidden** - campo que fica aparentemente apagado, mas quando envio ele enviará alguma informação.
  * **search** - campo para busca e com x para limpar campo, só funciona no chrome.
A funcionalidade de cada tipo de input vai depender de cada navegador.

