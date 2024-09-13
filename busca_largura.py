from collections import deque

# Definição do grafo
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

# Função para verificar se uma pessoa é um vendedor de manga
def pessoa_e_vendedor(nome):
    # Exemplo simples: considerar que uma pessoa é um vendedor se o último caractere do nome for m
    return nome[-1] == 'm'

# Função de pesquisa em largura
def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa.extend(grafo.get(nome, []))  # Usar get para evitar erro se o nome não estiver no grafo
    verificadas = set()  # Usar um conjunto para maior eficiência

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa.extend(grafo.get(pessoa, []))  # Usar get para evitar erro se a pessoa não estiver no grafo
                verificadas.add(pessoa)

    return False

pesquisa("voce")
