import heapq

def uniform_cost_search(graph, start, goal):
    """
    Executa a busca de custo uniforme (UCS) em um grafo representado como um dicionário.
    
    :param graph: Dicionário onde as chaves são os nós e os valores são listas de tuplas (vizinho, custo).
    :param start: Nó inicial.
    :param goal: Nó objetivo.
    :return: Custo mínimo e o caminho percorrido até o objetivo.
    """
    priority_queue = []  # Fila de prioridade
    heapq.heappush(priority_queue, (0, start, []))  # (custo, nó atual, caminho)
    visited = set()
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]
        
        if node == goal:
            return cost, path  # Retorna o custo e o caminho percorrido
        
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))
    
    return float("inf"), []  # Retorna infinito e um caminho vazio se não encontrar a solução

# Exemplo de uso:
graph = {
    'S': [('A', 8), ('B', 5)],
    'B': [('C', 7), ('D', 2)],
    'A': [('C', 3), ('F', 10)],
    'C': [('E', 2), ('F', 4)],
    'D': [('E', 2),],
    'E': [('G', 9)],
    'F': [('G', 2)],
    'G': []
}

start_node = 'S'
goal_node = 'G'

cost, path = uniform_cost_search(graph, start_node, goal_node)
print(f"Custo mínimo: {cost}")
print(f"Caminho percorrido: {path}")
