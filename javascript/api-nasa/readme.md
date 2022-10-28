# API - APOD

## Tecnologias

- HTML, CSS e Javascript

## Sobre

O projeto tem um input do tipo data e um butão, que faz a chamada pegando o valor do input e inserido na api.

### API

Link: [https://api.nasa.gov/](https://api.nasa.gov/)

### Solicitação HTTP

GET <https://api.nasa.gov/planetary/apod>

Somente assim irá exibir apenas a imagem do dia atual. </br>
Mas como precisamos passar a data inserida no input, ficaria assim:

GET <https://api.nasa.gov/planetary/apod&date=AAAA-MM-DD>

### Referencias

- <https://sophiali.dev/javascript-fetch-api-with-nasa-api>
- <https://acervolima.com/como-obter-dados-de-agencias-federais-da-nasa-usando-as-apis-publicas-da-nasa/>
