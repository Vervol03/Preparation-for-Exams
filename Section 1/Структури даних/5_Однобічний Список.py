"""
 Однозв'язний список - це структура даних, яка складається з вузлів, де кожен вузол 
                       містить дані та посилання на наступний вузол у списку. На відміну 
                       від двозв'язних списків, тут кожен вузол знає лише про наступний 
                       вузол, а не і про попередній.

 Основні операції, які можна виконувати з однозв'язним списком:
    Вставка (додавання) елемента:
        prepend - Додавання елемента на початок списку.
        append - Додавання елемента в кінець списку.
        insert_after - Додавання елемента після певного елемента у списку.
        insert_at - Додавання елемента до певної позиції у списку.
    
    Видалення елемента:
        remove_first - Видалення першого елемента у списку.
        remove_last - Видалення останнього елемента у списку.
        remove_by_value - Видалення певного елемента за значенням.
        remove_at - Видалення елемента за індексом.
        remove_repeat - Видалення елемента які повторюються.
    
    Отримання елемента:
        get_first - Отримання першого елемента у списку.
        get_last - Отримання останнього елемента у списку.
        get_at - Отримання елемента за індексом.
    
    Зміна значення елемента:
        set_at - Зміна значення певного елемента за індексом.
        set_by_value - Зміна значення певного елемента за значенням.
    
    Перевірка наявності елемента:
        contains - Перевірка, чи присутній певний елемент у списку.
    
    Отримання довжини списку:
        length - Отримання кількості елементів у списку.
"""


class Node:
    def __init__(self, data):
        self.data = data    # дані вузла
        self.next = None    # посилання на наступний вузол списку


class LinkedList:
    def __init__(self):
        self.head = None

    ###################################_ADD_METODS_###################################

    def prepend(self, new_data):
        old_head = self.head
        self.head = Node(new_data)
        self.head.next = old_head

    def append(self, new_data):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(new_data)
        else:
            self.head = Node(new_data)

    def insert_after(self, prev, new_data):
        if self.head:
            current = self.head
            while current:
                if prev == current.data:
                    temp = current.next
                    current.next = Node(new_data)
                    current.next.next = temp
                    return
                current = current.next
            print(f"Значення {prev} немає у списку!")
        else:
            print(f"Cписок порожній!")


    def insert_at(self, index, new_data):
        if self.head:
            current = self.head
            count = 1
            while current.next and count < index:
                current = current.next
                count += 1
            if count == index:
                tail = current.next
                current.next = Node(new_data)
                current.next.next = tail
            else:
                print(f"Индекс {index} великий для списку!")
        else:
            if index != 0:
                print(f"Индекс {index} великий для списку!")
            else:
                self.head = Node(new_data)


    ###################################_DEL_METODS_###################################

    def remove_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print(f"Неможна видалити елемент, Cписок порожній!")

    def remove_last(self):
        if self.head:
            if self.head.next:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None
            else:
                self.head = None
        else:
            print(f"Неможна видалити елемент, Cписок порожній!")

    def remove_by_value(self, value):
        if self.head:
            if self.head.data == value:
                self.head = self.head.next
            else:
                current = self.head
                while current.next:
                    if value == current.next.data:
                        current.next = current.next.next
                        return
                    current = current.next
                print(f"Значення {value} немає у списку!")
        else:
            print(f"Неможна видалити елемент, Cписок порожній!")

    def remove_at(self, index):
        if self.head:
            if index == 0:
                self.head = self.head.next
            else:
                current = self.head
                count = 0
                while current.next:
                    if count == index-1:
                        current.next = current.next.next
                        return
                    current = current.next
                    count += 1
                print(f"Индекс {index} великий для списку!")
        else:
            print(f"Неможна видалити елемент, Cписок порожній!")

    def remove_repeat(self):
        if self.head:
            current = self.head
            repeat = [current.data]
            while current.next:
                if current.next.data not in repeat:
                    repeat.append(current.next.data)
                    current = current.next
                else:
                    current.next = current.next.next
        else:
            print("Cписок порожній!")


    ###################################_GET_METODS_###################################

    def get_first(self):
        if self.head:
            return self.head.data
        print(f"Cписок порожній!")
    
    def get_last(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            return current.data
        print(f"Cписок порожній!")
    
    def get_at(self, index):
        if self.head:
            current = self.head
            count = 0
            while current:
                if index == count:
                    return current.data
                current = current.next
                count += 1
            print(f"Индекс {index} великий для списку!")
        else:
            print(f"Cписок порожній!")


    ###################################_SET_METODS_###################################

    def set_at(self, index, new_data):
        if self.head:
            current = self.head
            count = 0
            while current:
                if index == count:
                    current.data = new_data
                    return
                current = current.next
                count += 1
            print(f"Индекс {index} великий для списку!")
        else:
            print(f"Cписок порожній!")

    def set_by_value(self, data, new_data):
        if self.head:
            current = self.head
            while current:
                if data == current.data:
                    current.data = new_data
                current = current.next
        else:
            print(f"Cписок порожній!")
    

    ##################################################################################

    def contains(self, data):
        if self.head:
            current = self.head
            while current:
                if data == current.data:
                    return True
                current = current.next
            return False
        else:
            return False

    def length(self):
        if self.head:
            current = self.head
            count = 0
            while current:
                current = current.next
                count += 1
            return count
        else:
            return 0

    ##################################################################################

    def __repr__(self):
        linked = []; current_top = self.head
        while current_top:
            linked.append(current_top.data)
            current_top = current_top.next
        return str(linked)
    #________________________________________________________________________________#



if __name__ == "__main__": # Приклад використання

    Linked = LinkedList()

    # Додавання елементів у список:
    Linked.prepend(1)   # Додавання на 
    Linked.prepend(0)   # початок списку
    Linked.append(2)    # Додавання на 
    Linked.append(3)    # кинець списку
    Linked.insert_after(3, 4)   # Додавання після 
    Linked.insert_after(4, 5)   # вказаного значення
    Linked.insert_at(6, 6)  # Додавання за 
    Linked.insert_at(7, 7)  # вказаним індексом 

    print(Linked)

    # Видалення елементів зі списку:
    Linked.remove_first()   # Видалення першого елементу
    Linked.remove_last()    # Видалення останнього елементу
    Linked.remove_by_value(1)   # Видалення елемента за значенням
    Linked.remove_at(2)     # Видалення елемента за індексом
    Linked.remove_repeat()  # Видалення елемента які повторяються

    print(Linked)

    # Отримання елемента зі списку:
    print(Linked.get_first())   # Отримання першого елементу
    print(Linked.get_last())    # Отримання останнього елементу
    print(Linked.get_at(5))     # Отримання елементу за індексом
    
    print(Linked)

    # Зміна значення елемента:
    Linked.set_at(0, 0)     # Зміна значення елементу 
    Linked.set_at(1, 1)     # за індексом
    Linked.set_by_value(5, 2)   # Зміна значення елементу
    Linked.set_by_value(6, 3)   # за значення 

    print(Linked)

    # Получение даних:
    print(Linked.contains(1))   # Перевірка, чи присутній
    print(Linked.contains(4))   # певний елемент у списку
    print(Linked.length())  # Довжина списку