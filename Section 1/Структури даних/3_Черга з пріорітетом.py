"""
 Черга з пріоритетом - це варіація звичайної черги, в якій кожен елемент має свій пріоритет. 
                       При видаленні елемента з черги, він видаляється не в порядку його додавання, 
                       а в порядку його пріоритету. Елементи з більшим пріоритетом видаляються першими.
 
 Як я зрозумів це черга в якій елементи сортуються за ключем при додавані нового елементу.

 Основні операції, які можна виконувати з чергою з пріоритетом, включають:
    Enqueue: Додавання елемента з вказаним пріоритетом до черги.
    Dequeue: Видалення елемента з найвищим пріоритетом з черги.
    Peek: Перегляд елемента з найвищим пріоритетом без його видалення.
    Empty: Перевірка, чи є черга з пріоритетом порожньою.
"""


class Node:
    # Допоміжний клас - вузол черги.

    def __init__(self, item, priority):
        self.item = item   # поле для зберігання навантаження
        self.priority = priority  # поле для зберігання пріоритету
        self.next = None   # посилання на наступний вузол черги


class PriorityQueue:
    # Клас, що реалізує чергу з пріоритетом

    def __init__(self):
        self.front = None   # Посилання на початок черги
    
    def empty(self):
        return self.front is None
    
    def enqueue(self, item, priority):
        new_node = Node(item, priority)  # Створюємо новий вузол черги

        if self.empty() or priority > self.front.priority:
            new_node.next = self.front  # Якщо черга порожня або новий елемент має вищий пріоритет,
            self.front = new_node       # то робимо його початком черги
        else:   # Інакше знаходимо відповідне місце для вставки
            current = self.front
            while current.next and priority <= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.empty():
            raise Exception("PriorityQueue: 'dequeue' applied to empty container")
    
        current_front = self.front      # запам'ятовуємо поточну голову черги
        item = current_front.item       # запам'ятовуємо навантаження першого вузла
        self.front = self.front.next    # замінюємо перший вузол наступним
        del current_front   # видаляємо запам'ятований вузол

        if self.front is None:  # Якщо голова черги стала порожньою
            self.back = None    # Черга порожня = хвіст черги теж порожній
        
        return item
    
    def peek(self):
        if self.empty():
            raise Exception("PriorityQueue: 'peek' applied to empty container")
        
        return self.front.item
    
    def __repr__(self):
        queue = [] 
        current_top = self.front    # копіюємо поточну верхівку черги

        while current_top:  # перебираэмо чергу поки не сустрынемо None
            queue.append((current_top.item, current_top.priority))  # запам'ятовуємо кожний елемент з пріоритетом
            current_top = current_top.next  # переходимо до наступного вузла
        
        return str(queue)



if __name__ == "__main__": # Приклад використання

    queue = PriorityQueue()

    print(queue.empty())

    queue.enqueue("Клієнт 1", 3); print(queue)   # [('Клієнт 1', 3)]
    queue.enqueue("Клієнт 2", 4); print(queue)   # [('Клієнт 2', 4), ('Клієнт 1', 3)]
    queue.enqueue("Клієнт 3", 1); print(queue)   # [('Клієнт 2', 4), ('Клієнт 1', 3), ('Клієнт 3', 1)]
    queue.enqueue("Клієнт 4", 2); print(queue)   # [('Клієнт 2', 4), ('Клієнт 1', 3), ('Клієнт 4', 2), ('Клієнт 3', 1)]

    print(queue.dequeue())  # Клієнт 2
    print(queue.dequeue())  # Клієнт 1
    print(queue.dequeue())  # Клієнт 4
    print(queue.dequeue())  # Клієнт 3
