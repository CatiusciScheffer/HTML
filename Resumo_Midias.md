### Resumo de mídias em HTML

#### O que são tags de mídia
Tudo que está relacionado a áudio e vídeo.

>#### tag img
**Atributos**:
* **src**: "local/nome.extensão"
* **width**: "200", se utilizar sozinho vai escalar a imagem de forma dinâmica entre largura e altura.
* **height**: "200", em conjunto com width vai forçar a largura e altura definido podendo distorcer a imagem.
* **title**: quando passamos o mouse em cima mostra o titulo.
* **alt**: utilizado para acessibilidade, robôs inteligentes conseguem ler esta informação, e se caso a imagem não carregar este texto pode descrever o que deveria aparece.
* **sizes**: Especifica tamanhos de imagem para diferentes layouts de página.
* **srcset**: Especifica uma lista de arquivos de imagem para usar em diferentes situações.
**Exemplo de uso sizes e srcset**:
~~~html
<img srcset="img-300w.jpg 300w,
	     img-400w.jpg 400w,
	     img-600w.jpg 600w,
	     img-800w.jpg 800w"
     sizes="(max-width: 799px) 100vw, (min-width: 800px) 800px"
     src="img-800w.jpg">
     <!--Este exemplo é excelente para utilizar imagens de tamanhos diferentes e tornando responsivo-->
~~~

* **Observações**:
  * Arquivos de imagem **svg** não perdem resolução.
  * Se omitidas as informações de altura e largura vai ser carregado o tamanho do arquivo.

>#### tag audio



>#### tag video

>#### tag track

>#### tag iframe

