import networkx as nx

# Crea un grafo vacío
G = nx.Graph()

# Agrega nodos y aristas al grafo
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'A', weight=3)


# Encuentra el árbol de expansión mínima
M = nx.minimum_spanning_tree(G)

# Imprime el árbol de expansión mínima
print(M)