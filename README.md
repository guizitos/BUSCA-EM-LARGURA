# Busca em Largura para Encontrar um Vendedor de Manga

Este repositório contém um algoritmo de **busca em largura (BFS)** implementado em Python, que percorre um grafo social para encontrar um "vendedor de mangas". O vendedor, neste exemplo, é uma pessoa cujo nome termina com a letra `'m'`. O código simula uma rede de pessoas conectadas e realiza a busca a partir de um ponto inicial.

## Estrutura do Código

### 1. Definição do Grafo

O grafo é representado por um dicionário Python, onde:

- As **chaves** são os nomes das pessoas.
- Os **valores** são listas de outras pessoas que estão diretamente conectadas a elas.

Exemplo:

```python
grafo = {
    "voce": ["Bob", "Claire", "Alice"],
    "Bob": ["Anuj", "Peggy"],
    "Alice": ["Peggy"],
    "Claire": ["Thom", "Jonny"],
    "Anuj": [],
    "Peggy": [],
    "Thom": [],
    "Jonny": []
}
