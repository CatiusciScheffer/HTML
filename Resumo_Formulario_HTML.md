### Resumo Formulário HTML

#### Tag **&lt;form>**
##### Propriedade desta tag:
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
  * **button** - é aconselhavel uso da tag &lt;button&gt; por ser mais intuitivo atendento o quesito semântico do HTML5.
  * **range** - barra de progrresso, com propriedade:
    * min;
    * max;
  * **color** - cria uma caixa de seleção de cor;
  * **e-mail** - cria campo de e-mail obrigando preenchimento com @;
  * **url** - campo próprio para inserção de url, com restrição de preenchimento.
  * **date** - abre um calendário conforme navegador;
  * **week** - calendário de semana;
  * **month** - calendário de mês;
  * **checkbox** - cria caixa de seleção, que permite a **seleção de vários** ao mesmo tempo, abaixo as propiedades principais;
    * name - esta inforamção serve para agrupar os check, como ele aceita vários checkbox com mesmo **name**, então é enviado para o servidor o **'name'**=**'value'**, sendo vário valores, será necessário transformar esse name em uma lista para receber vários valores, basta colocar os colchetes após o nome, desta forma: **name=nomeexemplo[ ]**
    * disabled - deixa o checkbox aparente, mas desabilitado para marcação.
  * **radio** - caixa de seleção, mas ao contrário do checkbox **apenas uma opção** pode ser selecionado, as caixas para funcionarem deverão ter o mesmo **name** para agrupar e funcionar a marcação apenas no item desejado;
  * **file** - campo para anexar um arquivo.
    * multiple - para escolher vários arquivos, se não atribuir esta propriedade o padrão é poder escolher apenas um arquivo.
  * **hidden** - campo que fica aparentemente apagado, mas quando envio ele enviará alguma informação.
  * **search** - campo para busca e com x para limpar campo, só funciona no chrome.
A funcionalidade de cada tipo de input vai depender de cada navegador.

#### Button
* A tag utilizada para criação de um botão é a tag **&lt;button&gt;** essa tega têm três parâmetros que modificam o comportamento do botão.
  * Parâmetro **type =**
    * **"button"** só vai funcionar se utilizar o java script para adicionar um evento, existem vários eventos;
    ~~~html
    <button type="button" onclick="alert('Clique aqui.')">Clique</button>
    ~~~
    * **"reset"** limpa os campos de onde este botão estiver dentro.
    ~~~html
      <button type="reset">Limpar</button>
      ~~~
    * **"submit"** envia o formulário, finaliza o preenchimento do formulário, o botão enter já age como evento submit.
    ~~~html
      <button type="submit">Enviar</button>
    ~~~

#### Select Box
Lista pré-definida para o usuário escolher uma ou algumas opções, cria uma caixa de seleção com uma lista dos itens pré-definidos utilizando a tag **&lt;select&gt;** para criar a caixa toda, e cada item pré-definido da listagem é criado pela tag **&lt;option&gt;** conform exemplo abaixo:
~~~html
  <select name="role"><!--Pode se ter vários selects, e seu funcionamento se difere pelo nome-->
    <option value="">Selecione uma opção</option><!--Este valor em branco e este texto vão ficar aparente quando formulário é aberto-->
    <option value="auxiliar">Estagiário</option>
    <option value="gerente">Gerente</option>
    <option value="diretor">Diretor</option>
    <option value="socio">Sócio</option>
  </select>
~~~
* Utilizando parâmetro para múltiplas escolhas dentro dos itens pré-definidos através do atributo **_multiple_**, conforme exemplo:
  ~~~html
    <select name="multiple" multiple>
      <option value="">Selecione a/as opções</option>
      <option value="auxiliar">Chocolate Branco</option>
      <option value="gerente">Morango</option>
      <option value="diretor">Cocô</option>
      <option value="socio">Nutella</option>
    </select>
  ~~~
* Utilizando parâmetro **selected** para deixar um dos valores da caixa de listagem como valor padrão na abertura do formulário:
  ~~~html
  <select name="select">
    <option value="auxiliar">Estagiário</option>
    <option value="gerente" selected>Gerente</option><!--utilizado nesta linha-->
    <option value="diretor">Diretor</option>
    <option value="socio">Sócio</option>
  </select>
  ~~~
#### Text Area
Campo para envio de mensagens de texto maiores do que um campo de input por exemplo. Tendo a possibilidade de ajuste da largura pelo atributo **cols** e da altura pelo atributo **rows**, podendo também ser definido pelo css.
~~~html
<textarea name="texto" cols="30" rows="10">Deixe aqui sua mensagem.</textarea>
~~~
