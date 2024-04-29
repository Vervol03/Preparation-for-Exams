"""
 Стек - це структура даних, яка працює за принципом "останній прийшов, 
        першим вийшов" (Last In, First Out, LIFO). Це означає, що останній 
        елемент, доданий до стеку, буде першим, який буде видалений.

 Основні операції, які можна виконувати зі стеком, включають:
    Push: Додавання елемента до вершини стеку.
    Pop: Видалення елемента з вершини стеку.
    Top: Перегляд елемента на вершині стеку без його видалення.
    Empty: Перевірка, чи є стек порожнім.
"""


class Node:
    # Допоміжний клас, що реалізує вузол стеку

    def __init__(self, item):
        self.item = item    # створюєм поле для зберігання навантаження
        self.next = None    # посилання на наступний вузол стеку


class Stack:
    # Клас, що реалізує стек елементів як рекурсивну структуру
    
    def __init__(self):
        self.top_node = None # посилання на верхівку стеку

    def empty(self):  # Перевіряє чи стек порожній
        return self.top_node is None
 
    def push(self, item): # Додає елемент у стек
        new_node = Node(item)               # Створюємо новий вузол стеку
        if not self.empty():                # Якщо стек не порожній, то новий вузол
            new_node.next = self.top_node   # має посилатися на поточну верхівку
        
        self.top_node = new_node # змінюємо верхівку стека новим вузлом
 
    def pop(self):
        if self.empty(): # Якщо стек порожній
            raise Exception("Stack: 'pop' applied to empty container")
        
        current_top = self.top_node         # запам'ятовуємо поточну верхівку стека
        item = current_top.item             # запам'ятовуємо навантаження верхівки
        self.top_node = self.top_node.next  # замінюємо верхівку стека наступним вузлом

        del current_top  # видаляємо запам'ятований вузол, що місить попередню верхівку
        return item

    def top(self):  # Повертає верхівку стека
        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        return self.top_node.item
    
    def __repr__(self):
        stack = [] 
        current_top = self.top_node  # копіюємо поточну верхівку стека

        while current_top:  # перебираэмо стек поки не сустрынемо None
            stack.append(current_top.item)  # запам'ятовуємо кожний елемент
            current_top = current_top.next  # переходимо до наступного вузла
        
        return str(stack)


def bracketsChecker(brackets_sequence):
    s = Stack() # Створюємо порожній стек

    for bracket in brackets_sequence:
        if bracket == "(": 
            s.push(bracket)  # Потенційний початок контейнера
        else:
            if s.empty(): 
                return False # Дужкова послідовність не правильна
            else: 
                s.pop()      # Прибираємо контейнер з розгляду
    
    return s.empty()



if __name__ == "__main__": # Приклад використання

    for i in ('(()())', '(()()()())', '((()))', ')()(', '(((()', '())))'):
        print('%10s ->'%(i), bracketsChecker(i))

    s = Stack()
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)

    print(s)

    print(s.top())
    print(s.top())
    print(s.empty())

    print(s.pop())
    print(s.pop())

    print(s)

    print(s.pop())
    print(s.pop())
    print(s.empty())

    print(s)
