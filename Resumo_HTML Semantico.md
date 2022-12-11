### HTML Semântico

Tag &lt;main>

Essa tag não pode ser filha de &lt;header>, &lt;foooter>, &lt;article> e só poderá haver uma tag &lt;main> no documentos html.

Tag &lt;section>
Quando não houver uma tag semântica específica poderá ser utilizado, mas não usar apenas para separar estilização, faz parte da estrutura e ajuda nas buscar.

Tag &lt;aside>
Deve conter assuntos separados do conteúdo principal, assuntos a parte.

Tag &lt;article>
Conteúdo poderá ser aninhado, todos os filhos ficam relacionados ao pai. Dentro podemos utilizar a tag &lt;time> com atributo **pubdate** para colocar a data da publicação.
Se for necessário colocar uma citação dentro do article utilizo a Tag &lt;blockquote> com atributo **cite="url"** para vincular a fonte da informação. A tag &lt;blockquote> quebra a linha, se quiser fazer uma citação sem quebra de linha utilizo a tag &lt;q>;

Tag &lt;figure>
Essa tag é um container, a tag &lt;figcaption> serve para adicionar a legenda à imagem que vai ter dentro da figure, ou seja a tag &lt;img>, a tag &lt;figcaption> dentro a tag &lt;figure> ficam conectadas, o que facilitam as buscar também.

Tag &lt;picture> funciona como a tag &lt;figure>, mas quando é necessário carregar uma imagem para cada tamanho de tela isso só serápossível na tag &lt;picture> com atributo **media**.