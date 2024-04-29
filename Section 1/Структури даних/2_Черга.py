"""
 Черга - це структура даних, що працює за принципом "перший прийшов, перший 
         вийшов" (First In, First Out, FIFO). Це означає, що елемент, 
         який доданий першим, буде першим, який буде видалений.

 Основні операції, які можна виконувати з чергою, включають:
    Enqueue: Додавання елемента до кінця черги.
    Dequeue: Видалення елемента з початку черги.
    Peek: Перегляд елемента на початку черги без його видалення.
    Empty: Перевірка, чи є черга порожньою.
"""

class Node:
    # Допоміжний клас - вузол черги.

    def __init__(self, item):
        self.item = item   # поле для зберігання навантаження
        self.next = None   # посилання на наступний вузол черги


class Queue:
    # Клас, що реалізує чергу елементів як рекурсивну структуру

    def __init__(self):
        self.front = None   # Посилання на початок черги
        self.back = None    # Посилання на кінець черги
    
    def empty(self):
        return self.front is None and self.back is None
    
    def enqueue(self, item):
        new_node = Node(item)   # Створюємо новий вузол черги
        if self.empty():            # Якщо черга порожня
            self.front = new_node   # новий вузол робимо початком черги
        else:
            self.back.next = new_node # останній вузол черги посилається на новий вузол
        
        self.back = new_node # Останній вузол вказує на новий вузол

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")
    
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
        stack = [] 
        current_top = self.front  # копіюємо поточну верхівку стека

        while current_top:  # перебираэмо стек поки не сустрынемо None
            stack.append(current_top.item)  # запам'ятовуємо кожний елемент
            current_top = current_top.next  # переходимо до наступного вузла
        
        return str(stack)



if __name__ == "__main__": # Приклад використання

    queue = Queue()

    print(queue.empty()) # True

    queue.enqueue("Клієнт 1")
    queue.enqueue("Клієнт 2")
    queue.enqueue("Клієнт 3")
    queue.enqueue("Клієнт 4")

    print(queue.peek()) # Клієнт 1
    print(queue.peek()) # Клієнт 1
    print(queue.peek()) # Клієнт 1

    print(queue) # ['Клієнт 1', 'Клієнт 2', 'Клієнт 3', 'Клієнт 4']

    print(queue.empty())    # False
    print(queue.dequeue())  # Клієнт 1
    print(queue.dequeue())  # Клієнт 2

    print(queue)    # ['Клієнт 3', 'Клієнт 4']

    print(queue.dequeue())  # Клієнт 3
    print(queue.dequeue())  # Клієнт 4
    print(queue.empty())    # True

    print(queue)    # []