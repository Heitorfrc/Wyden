

def tipo_grafo_euleriano(grafo):
    # Contar os graus dos vértices
    graus = {v: 0 for v in grafo}
    for v in grafo:
        for vizinho in grafo[v]:
            graus[v] += 1

    # Contar vértices com grau ímpar
    vertices_impares = sum(1 for grau in graus.values() if grau % 2 != 0)

    if vertices_impares == 0:
        return "O grafo é euleriano."
    elif vertices_impares == 2:
        return "O grafo é semi-euleriano."
    else:
        return "O grafo não é euleriano."

# Exemplo de um grafo com 4 vertices
grafo_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

resultado = tipo_grafo_euleriano(grafo_exemplo)
print(resultado)

# Mais um exemplo de um grafo com 4 vertices
grafo_exemplo2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['C', 'B']
}

resultado2 = tipo_grafo_euleriano(grafo_exemplo2)
print(resultado2)

# Terceiro exemplo de um grafo com 4 vertices
grafo_exemplo3 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}

resultado3 = tipo_grafo_euleriano(grafo_exemplo3)
print(resultado3)