# Curso da biblioteca Matplotlib.Pyplot

Notas :
--

Documentação oficial do Matplotlib
A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).

Cada um deles é opcional. Se não fornecido, o valor do ciclo de estilo é usado. Exceção: se a linha for dada, mas não houver marcador, os dados serão uma linha sem marcadores.

Outras combinações como **[color] [maker] [line]** também são suportadas, mas observe que sua análise pode ser ambígua.
```
color: cor (ver exemplos abaixo)

label: rótulo

linestyle: estilo de linha (ver exemplos abaixo)

linewidth: largura da linha

marker: marcador (ver exemplos abaixo)
```

### Markers:

'.' point marker

','	pixel marker

'o'	circle marker

'v'	triangle_down marker

'^'	triangle_up marker

'<'	triangle_left marker

'>'	triangle_right marker

'1'	tri_down marker

'2'	tri_up marker

'3'	tri_left marker

'4'	tri_right marker

's'	square marker

'p'	pentagon marker

'*'	star marker

'h'	hexagon1 marker

'H'	hexagon2 marker

'+'	plus marker

'x'	x marker

'D'	diamond marker

'd'	thin_diamond marker

'|'	vline marker

'_'	hline marker


### Line Styles:

'-'	solid line style

'--'	dashed line style

'-.'	dash-dot line style

':'	dotted line style


### Colors:

As abreviações de cores suportadas são os códigos de uma letra.

'b'	blue

'g'	green

'r'	red

'c'	cyan

'm'	magenta

'y'	yellow

'k'	black

'w'	white

```
Se a cor for a única parte da string de formato, você poderá usar adicionalmente qualquer especificação matplotlib.colors, por exemplo, nomes completos **('green')** ou seqüências de caracteres hexadecimais **('# 008000')**.
```

Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
