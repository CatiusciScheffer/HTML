### Resumo de mídias em HTML

#### O que são tags de mídia
Tudo que está relacionado a áudio e vídeo.

>#### tag img
A tag **&lt;img&gt;** é usada para incorporar uma imagem em uma página HTML.

As imagens não são tecnicamente inseridas em uma página da web; as imagens estão vinculadas a páginas da web. A tag &lt;img&gt; cria um espaço de retenção para a imagem referenciada.

A tag &lt;img&gt; tem dois atributos obrigatórios:

    src - Especifica o caminho para a imagem
    alt - Especifica um texto alternativo para a imagem, se a imagem por algum motivo não puder ser exibida

Observação: Além disso, sempre especifique a largura e a altura de uma imagem. Se largura e altura não forem especificadas, a página pode piscar enquanto a imagem é carregada.

Para vincular uma imagem a outro documento, basta aninhar a tag &lt;img&gt; dentro de uma tag **&lt;a&gt;** (veja o exemplo abaixo).

**Atributos**:
* **width**: "200", se utilizar sozinho vai escalar a imagem de forma dinâmica entre largura e altura.
* **height**: "200", em conjunto com width vai forçar a largura e altura definido podendo distorcer a imagem.
* **title**: quando passamos o mouse em cima mostra o titulo.
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
A tag **&lt;audio&gt;** é usada para incorporar conteúdo de som em um documento, como música ou outros fluxos de áudio.

A tag &lt;audio&gt; contém uma ou mais tags <source> com diferentes fontes de áudio. O navegador escolherá a primeira fonte compatível.

O texto entre as tags &lt;audio&gt; e &lt;/audio&gt; só será exibido em navegadores que não suportam o elemento &lt;audio&gt;.

Existem três formatos de áudio suportados em HTML: MP3, WAV e OGG.

**Atributos:**
* **autoplay**: toca o som automáticamente ao carregar o navegador;
* **controls**: mostra os botões de controle de volume, velocidade e tempo.
  * **tag filha**:
    * **source**:
      * atributo: **src**, ou seja caminho do arquivo de áudio;

**Exemplo de código:**
~~~html
  <audio controls autoplay>
    <source src="horse.ogg" type="audio/ogg">
    <source src="horse.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio> 
~~~

**Tipos de Arquivos de Áudio (atributo "type")**

|Formato Arquivo|Tipo de Mídia|
|-|-|
|MP3|audio/mpeg|
|OGG|audio/ogg|
|WAV|audio/wav|

>#### tag video
A tag **&lt;video&gt;** é usada para incorporar conteúdo de vídeo em um documento, como um clipe de filme ou outros fluxos de vídeo.

A tag &lt;video&gt; contém uma ou mais tags <source> com diferentes fontes de vídeo. O navegador escolherá a primeira fonte compatível.

O texto entre as tags &lt;video&gt; e &lt;/video&gt; só será exibido em navegadores que não suportam o elemento &lt;video&gt;.

Existem três formatos de vídeo suportados em HTML: MP4, WebM e OGG.

**Atributos:**
* **autoplay**: começa o vídeo automáticamente ao carregar o navegador;
* **controls**: mostra os botões de controle de volume, velocidade e tempo.
  * **tag filha**:
    * **source**:
      * atributo: **src**, ou seja caminho do arquivo de vídeo;
**Tipos de Arquivos de Vídeo (atributo "type")**

|Formato Arquivo|Tipo de Mídia|
|-|-|
|MP4|video/mp4|
|WebM|video/webm|
|OGG|video/ogg|
**Exemplo de código**
~~~html
  <video width="320" height="240" controls>
    <source src="movie.mp4" type="video/mp4">
    <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
  </video> 
~~~

>#### tag track
Este elemento é usado para especificar legendas, arquivos de legenda ou outros arquivos contendo texto, que devem estar visíveis quando a mídia estiver sendo reproduzida.

As trilhas são formatadas no formato WebVTT (arquivo.vtt), então é necessário além do arquivo de áudio ou vídeo, mais o arquivo vtt que é a legenda.

~~~html
  <video width="320" height="240" controls>
    <source src="forrest_gump.mp4" type="video/mp4">
    <source src="forrest_gump.ogg" type="video/ogg">
    <track src="fgsubtitles_en.vtt" kind="subtitles" srclang="en" label="English">
    <track src="fgsubtitles_no.vtt" kind="subtitles" srclang="no" label="Norwegian">
  </video>
~~~
O atributo kind com valor descriptions pode ser usado como uma narração do que acontece para acessibilidade, então o texto colocado servirá de narração pelos equipamentos adaptados.

>#### tag iframe
A tag **&lt;iframe&gt;** especifica um quadro embutido.

Um quadro embutido é usado para incorporar outro documento no documento HTML atual.

Podemos usar o CSS para estilizar o &lt;iframe&gt;.

É uma boa prática sempre incluir um atributo de título para o &lt;iframe&gt;. Isso é usado por leitores de tela para ler qual é o conteúdo do &lt;iframe&gt;.
**Exemplo de código:**
~~~html
  <iframe src="/default.asp" width="100%" height="300" style="border:1px solid black;">
  </iframe>

  <iframe src="/default.asp" width="100%" height="300" style="border:none;">
  </iframe> 
~~~
