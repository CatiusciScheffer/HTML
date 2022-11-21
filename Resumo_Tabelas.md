Resumo Tabelas HTML

TAG **&lt;table&gt;**
Utilizada para criar uma tabela no HTML.
Uma tabela HTML consiste em um elemento &lt;table> e um ou mais elementos &lt;tr>, &lt;th> e &lt;td>.
O elemento &lt;tr> define uma linha da tabela, o elemento &lt;th> define um cabeçalho da tabela e o elemento &lt;td> define uma célula da tabela.

|**Tag**|**Descrption**|
|-|-|
|&lt;table&gt;|Define a tabela|
|&lt;th&gt;|Define cabeçalho da célula na tabela|
|&lt;tr&gt;|Define a linha na tabela|
|&lt;td&gt;|Define a célula na tabela|
|&lt;caption&gt;|Define um título pra tabela|
|&lt;colgroup&gt;|Especifica um grupo de uma ou mais colunas em uma tabela para formatação.|
|&lt;col&gt;|Especifica propriedades de coluna para cada coluna dentro de um elemento &lt;colgroup&gt;|
|&lt;thead&gt;|Agrupa o conteúdo do cabeçalho em uma tabela|
|&lt;tbody&gt;|Agrupa o conteúdo do corpo em uma tabela|
|&lt;tfoot&gt;|Agrupa o conteúdo do rodapé em uma tabela|

Definição das tags **&lt;colgroup&gt;** com **&lt;col&gt;**
A tag &lt;colgroup&gt; é útil para aplicar estilos a colunas inteiras, em vez de repetir os estilos para cada célula, para cada linha.

Observação: a tag &lt;colgroup&gt; deve ser filha de um elemento &lt;table&gt;, depois de qualquer elemento &lt;caption&gt; e antes de qualquer elemento &lt;thead&gt;, &lt;tbody&gt;, &lt;tfoot&gt; e &lt;tr&gt;.

Dica: Para definir propriedades diferentes para uma coluna dentro de um &lt;colgroup&gt;, use a tag &lt;col&gt; dentro da tag &lt;colgroup&gt;.
~~~html
<table>
        <colgroup>
          <col span="2" style="background-color:red">
          <col style="background-color:yellow">
          <!--
            span -> define número de colunar que terá este estilo
            style -> definições de estilo
          -->
        </colgroup>
        <tr>
          <th>ISBN</th>
          <th>Title</th>
          <th>Price</th>
        </tr>
        <tr>
          <td>3476896</td>
          <td>My first HTML</td>
          <td>$53</td>
        </tr>
      </table>
~~~

**MESCLAR CÉLULAR**
Basta utilizar os atributos nas tags &lt;td&gt; ou &lt;th&gt; **rowspan** para mesclar as célular na vertical ou **colspan** para mesclar célular na horizontal.
~~~html
    <!--MECLAR CABEÇALHO NA HORIZONTAL-->
    <tr>
        <th colspan="3">Mesclando linha</th>
    </tr>
    OU
    <!--MESCLAR CÉLUAS NA VERTICAL-->
    <tr>
        <td rowspan="3">Mesclando células</td>
        <td>My first HTML</td>
        <td>$53</td>
    </tr>
~~~