"""
    Граф - це абстрактна математична структура, яка складається з множини вершин (вузлів) 
           та множини ребер (зв'язків), які з'єднують ці вершини. 
           Граф може бути орієнтованим або неорієнтованим.

    Вершини (nodes, vertices): 
        Представляють собою елементи графа, які можуть мати певні 
        властивості або атрибути.
    
    Ребра (edges): 
        Представляють зв'язки між вершинами графа. Вони можуть мати напрямок (для 
        орієнтованого графа) або відсутній напрямок (для неорієнтованого графа).
    
    Орієнтований граф (directed graph): 
        Граф, в якому кожне ребро має напрямок, тобто з однієї вершини до іншої.
    
    Неорієнтований граф (undirected graph): 
        Граф, в якому ребра не мають напрямку, тобто зв'язок між двома вершинами є взаємним.

    Вага ребра (edge weight): 
        Це числове значення, яке відображає вартість або відстань між вершинами. 
        Вага може бути присутньою або відсутньою в залежності від типу графа та застосовуваних алгоритмів.
    
    МЕТОДИ:
    
    Пошук в ширину і глибину:
        Пошук в ширину (BFS) та пошук в глибину (DFS) - це алгоритми обходу графа.
        BFS - обходить граф рівень за рівнем, спочатку відвідуючи всі сусідні вершини від 
              початкової вершини, потім їх сусідів і так далі.
        DFS - переходить глибше в граф, відвідуючи всі сусідні вершини однієї гілки 
              перед тим, як повернутися та відвідати інші гілки.

    Пошук зв'язних компонентів:
        Це алгоритм, що визначає, які вершини графа є зв'язними між собою.
        Зазвичай використовується пошук в глибину або пошук в ширину для 
        визначення зв'язності між вершинами.

    Побудова кістякового дерева:
        Кістякове дерево - це підграф зв'язного графа, який є деревом.
        Алгоритми, такі як алгоритм Прима або алгоритм Краскала, 
        використовуються для побудови кістякового дерева.

    Побудова найкоротших шляхів з виділеної вершини:
        Це алгоритм, який знаходить найкоротші шляхи від однієї вказаної 
        вершини до всіх інших вершин у графі.
        Зазвичай використовується алгоритм Дейкстри або алгоритм Беллмана-Форда.

    Побудова найкоротших шляхів між двома вершинами:
        Це алгоритм, який знаходить найкоротший шлях між двома 
        вказаними вершинами у графі.
        Зазвичай використовується алгоритм Дейкстри або алгоритм A*(A-star).
"""

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
    
    ########################### Пошук зв'язних компонентів ###########################

    def find_connected_components(self):
        visited = set()
        connected_components = []
        for vertex in self.vertices:
            if vertex not in visited:
                component = []
                self._dfs_recursive(vertex, visited, component)
                connected_components.append(component)
        return connected_components
    
    ########################### Побудова кістякового дерева ###########################
    
    def prim_mst(self, start_vertex):
        mst = set()  # Кістякове дерево
        visited = set()  # Відвідані вершини
        heap = [(0, start_vertex, None)]  # Мінімальна купа для вибору наступної вершини

        def heapify(heap):
            n = len(heap)
            for i in range(n // 2 - 1, -1, -1):
                heapify_down(heap, i)

        def heapify_down(heap, i):
            n = len(heap)
            smallest = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < n and heap[left_child][0] < heap[smallest][0]:
                smallest = left_child
            if right_child < n and heap[right_child][0] < heap[smallest][0]:
                smallest = right_child
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                heapify_down(heap, smallest)

        def heappop(heap):
            if not heap:
                return None
            root = heap[0]
            heap[0] = heap[-1]
            del heap[-1]
            heapify_down(heap, 0)
            return root

        def heappush(heap, vertex):
            heap.append(vertex)
            i = len(heap) - 1
            while i > 0:
                parent = (i - 1) // 2
                if heap[parent][0] <= heap[i][0]:
                    break
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent

        heapify(heap)

        while heap:
            weight, current_vertex, parent = heappop(heap)
            if current_vertex not in visited:
                visited.add(current_vertex)
                if parent is not None:
                    mst.add((min(current_vertex, parent), max(current_vertex, parent)))
                for neighbor, edge_weight in self.vertices[current_vertex].neighbors.items():
                    if neighbor not in visited:
                        heappush(heap, (edge_weight, neighbor, current_vertex))
        return mst

    ################### Побудова найкоротших шляхів з виділеної вершини ###################

    def shortest_paths(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        unvisited_vertices = set(self.vertices.keys())
        while unvisited_vertices:
            current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
            unvisited_vertices.remove(current_vertex)
            current_distance = distances[current_vertex]
            for neighbor, edge_weight in self.vertices[current_vertex].neighbors.items():
                new_distance = current_distance + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        return distances

    ################### Побудова найкоротших шляхів між двома вершинами ###################

    def shortest_path(self, start_vertex, end_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        unvisited_vertices = set(self.vertices.keys())
        while unvisited_vertices:
            current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
            if current_vertex == end_vertex:
                break
            unvisited_vertices.remove(current_vertex)
            current_distance = distances[current_vertex]
            for neighbor, edge_weight in self.vertices[current_vertex].neighbors.items():
                new_distance = current_distance + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        return distances[end_vertex]

    #########################################################################################

    def print_graph(self):
        # Метод виводить інформацію про граф: вершини та їхніх сусідів
        for vertex in self.vertices:
            print("Вершина:", vertex)
            print("Сусіди:", [neighbor for neighbor in self.vertices[vertex].get_neighbors()])
            print("-----------------------")


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


    ########################### Пошук зв'язних компонентів ###########################

    # Створення нового незалежного графа
    vertex_L = Vertex('L')
    vertex_M = Vertex('M')

    graph.add_vertex(vertex_L)
    graph.add_vertex(vertex_M)

    graph.add_edge('L', 'M', 6)

    # Виклик методу для знаходження зв'язних компонент
    connected_components = graph.find_connected_components()
    print("\nЗв'язні компоненти:")
    for component in connected_components: print(component)


    ########################### Побудова кістякового дерева ###########################

    graph.add_edge('D', 'M',15)

    # Побудова кістякового дерева
    mst = graph.prim_mst('D')
    print("\nКістякове дерево (зв'язні ребра):")
    for edge in mst: print(edge)


    ################### Побудова найкоротших шляхів з виділеної вершини ###################

    # Побудова найкоротших шляхів
    shortest_paths = graph.shortest_paths('A')

    # Виведення найкоротших шляхів
    print("\nНайкоротші шляхи з вершини", shortest_paths)


    ################### Побудова найкоротших шляхів між двома вершинами ###################
    
    # Вершини між якими будуємо найкоротший шлях
    start_vertex = 'A'
    end_vertex = 'L'

    # Побудова найкоротшого шляху
    shortest_path_length = graph.shortest_path(start_vertex, end_vertex)

    # Виведення результату
    print(f"\nНайкоротший шлях між вершинами {start_vertex} та {end_vertex} має довжину {shortest_path_length}.")