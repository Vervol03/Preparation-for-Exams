"""
 Пошук з відсіканням (Pruning): Цей метод використовується у пошуку 
 найкоротшого шляху або оптимізації. Він дозволяє відкидати гілки пошуку, 
 які точно не приведуть до рішення або оптимального результату.
 Складність залежить від конкретної умови відсікання, але, як правило, 
 буде аналогічною складності алгоритму, який використовує цю умову.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
    def add_edge(self, node):
        self.edges.append(node)

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        self.nodes.append(Node(value))

    def add_edge(self, value1, value2):
        node1 = self.get_node(value1)
        node2 = self.get_node(value2)
        if node1 and node2:
            node1.add_edge(node2)
            node2.add_edge(node1)

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def dfs_with_pruning(self, start_value, condition):
        start_node = self.get_node(start_value)
        if not start_node:
            return []

        visited = set()
        stack = [start_node]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                result.append(node.value)
                visited.add(node)
                if condition(node):
                    for edge in node.edges:
                        if edge not in visited:
                            stack.append(edge)
        return result


if __name__ == "__main__":

    graph = Graph()

    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("DFS with pruning:", graph.dfs_with_pruning(0, lambda node: node.value <= 2))