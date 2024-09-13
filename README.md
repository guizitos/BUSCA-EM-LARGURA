# Busca em Largura para Encontrar um Vendedor de Manga

Este repositório contém um algoritmo de **busca em largura (BFS)** implementado em Python, que percorre um grafo social para encontrar um "vendedor de mangas". O vendedor, neste exemplo, é uma pessoa cujo nome termina com a letra `'m'`. O código simula uma rede de pessoas conectadas e realiza a busca a partir de um ponto inicial.

## Estrutura do Código

### 1. Definição do Grafo

O grafo é representado por um dicionário Python, onde:

- As **chaves** são os nomes das pessoas.
- Os **valores** são listas de outras pessoas que estão diretamente conectadas a elas.

Exemplo:

![Alt text](img1.png)

Aqui, a pessoa "voce" está conectada a "Bob", "Claire", e "Alice", e assim por diante.

### 2. Função para Verificar se Alguém é um Vendedor

A função `pessoa_e_vendedor(nome)` verifica se uma pessoa é considerada um vendedor de manga com base em uma regra simples: se o último caractere do nome for `'m'`, a pessoa é identificada como um vendedor.

