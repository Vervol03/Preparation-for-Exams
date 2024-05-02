class Vertex:
    def __init__(self, name):
        # Конструктор класу Vertex, приймає назву вершини і створює вершину з пустим списком сусідів.
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        # Метод додає сусіда для поточної вершини з вагою шляху до нього.
        self.neighbors[neighbor] = weight

    def get_neighbors(self):
        # Метод повертає список сусідів поточної вершини.
        return self.neighbors.keys()

    def get_name(self):
        # Метод повертає назву поточної вершини.
        return self.name

    def get_weight(self, neighbor):
        # Метод повертає вагу шляху до вказаного сусіда.
        return self.neighbors[neighbor]


class Graph:
    def __init__(self):
        # Конструктор класу Graph, створює порожній словник для зберігання вершин графа.
        self.vertices = {}

    ################################# Основні методи #################################

    def add_vertex(self, vertex):
        # Метод додає вершину до графа, перевіряючи, чи вершина є екземпляром класу Vertex та чи її назва ще не існує в графі.
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2, weight):
        # Метод додає ребро між двома вершинами з вказаною вагою.
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add_neighbor(vertex2, weight)
            self.vertices[vertex2].add_neighbor(vertex1, weight)
            return True
        else:
            return False
    
    ############################# Пошук в ширину і глибину #############################

    def bfs(self, start_vertex):  # Пошук в ширину 
        result = []
        visited = set()
        queue = [start_vertex] 
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                result.append(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.vertices[current_vertex].get_neighbors():
                    if neighbor not in visited:
                        queue.append(neighbor)
        print(' -> '.join(result))

    def dfs(self, start_vertex):    # Пошук в глибину 
        visited = set()
        result = self._dfs_recursive(start_vertex, visited)
        print(' -> '.join(result))
    
    def _dfs_recursive(self, current_vertex, visited, x = []):
        if current_vertex not in visited:
            x.append(current_vertex)
            visited.add(current_vertex)
            for neighbor in self.vertices[current_vertex].get_neighbors():
                self._dfs_recursive(neighbor, visited, x)
        return x


# Приклад використання
if __name__ == "__main__":

    # Створення графа
    graph = Graph()

    ################################# Основні методи #################################

    # Додавання вершин
    vertex_A = Vertex('A')
    vertex_B = Vertex('B')
    vertex_C = Vertex('C')
    vertex_D = Vertex('D')

    graph.add_vertex(vertex_A)
    graph.add_vertex(vertex_B)
    graph.add_vertex(vertex_C)
    graph.add_vertex(vertex_D)

    # Додавання ребер з вагами
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)

    # Виведення графа
    graph.print_graph()


    ############################# Пошук в ширину і глибину #############################

    # Виклик методу пошуку в ширину (BFS)
    print("\nПошук в ширину (BFS):")
    graph.bfs('B')

    # Виклик методу пошуку в глибину (DFS)
    print("\nПошук в глибину (DFS):")
    graph.dfs('B')