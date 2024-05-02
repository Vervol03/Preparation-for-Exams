"""
 Пошук в ширину (BFS) і Пошук у глибину (DFS): Ці методи використовуються для пошуку у графах. 
 BFS відвідує всі вершини на одному рівні графа перед переходом на наступний рівень, тоді як 
 DFS просувається "вглиб" графа, поки не знайде рішення або не дійде до кінця.
 Пошук в глибину (DFS):
    Часова складність: O(V + E), де V - кількість вершин, E - кількість ребер
    Рекурсивний або ітеративний алгоритм, що проходить крізь всі вершини та ребра графа.
 Пошук в ширину (BFS):
    Часова складність: O(V + E), де V - кількість вершин, E - кількість ребер
    Алгоритм, що працює на основі черги та обходить всі вершини та ребра графа.
"""

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue.extend(self.graph.get(node, []))

        return result

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                result.append(node)
                visited.add(node)
                stack.extend(reversed(self.graph.get(node, [])))

        return result



if __name__ == "__main__":

    graph = Graph()

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("BFS:", graph.bfs(2))
    print("DFS:", graph.dfs(2))
