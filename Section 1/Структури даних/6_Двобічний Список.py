"""
 Двоспрямований список - це структура даних, що складається з вузлів, 
                         кожен з яких містить посилання на наступний та 
                         попередній вузли в списку. Основна особливість 
                         цієї структури полягає в тому, що вона дозволяє 
                         переходити в обох напрямках, тобто як від початку 
                         до кінця, так і в зворотному напрямку.

 Основні методи двоспрямованого списку включають:
     Вставкаелемента:
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
        self.prev = None    # посилання на попередній вузол списку


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    ###################################_ADD_METODS_###################################

    def prepend(self, new_data):
        if not self.head: # 0
            self.head = Node(new_data)
            self.tail = self.head
        elif not self.head.next: # 1
            self.head = Node(new_data)
            self.head.next = self.tail
            self.tail.prev = self.head
        else: # > 1
            temp = self.head
            self.head = Node(new_data)
            temp.prev = self.head
            self.head.next = temp
 
    # Алгоритм аналогічний 'prepend' але замінені значення: head<=>tail; next<=>prev
    def append(self, new_data):
        if not self.tail: # 0
            self.tail = Node(new_data)
            self.head = self.tail 
        elif not self.tail.prev: # 1
            self.tail = Node(new_data)
            self.tail.prev = self.head
            self.head.next = self.tail
        else: # > 1
            temp = self.tail
            self.tail = Node(new_data)
            temp.next = self.tail
            self.tail.prev = temp

    def insert_after(self, old_data, new_data):
        if not self.head: 
            print(f"Cписок порожній!")
        elif not self.head.next: # 1
            if self.head.data == old_data:
                self.append(new_data)
            else:
                print(f"Значення {old_data} немає у списку!")
        else: # > 1
            if self.tail.data == old_data:
                self.append(new_data)
            else:
                current = self.head
                while current:
                    if old_data == current.data:
                        temp = current.next
                        current.next = Node(new_data)
                        temp.prev = current
                        current.next.next = temp
                        return
                    current = current.next
                print(f"Значення {old_data} немає у списку!")

    def insert_at(self, index, new_data):
        if not self.head: # 0
            if index == 0: 
                self.append(new_data)
            else: 
                print(f"Индек {index} великий для списку!")
        elif not self.head.next:
            if   index == 0: 
                self.prepend(new_data)
            elif index == 1: 
                self.append(new_data)
            else: 
                print(f"Индек {index} великий для списку!")
        else:
            if index == 0: 
                self.prepend(new_data)
                return
            current = self.head
            count = 0
            while current.next:
                if count+1 == index:
                    temp = current.next
                    current.next = Node(new_data)
                    temp.prev = current.next
                    current.next.next = temp
                    current.next.prev = current
                    return
                current = current.next
                count += 1
            if count+1 == index: 
                self.append(new_data)
                return
            print(f"Индек {index} великий для списку!")

    ###################################_DEL_METODS_###################################

    def remove_first(self):
        if not self.head:
            print(f"Cписок порожній!")
        elif not self.head.next:
            self.head = None
            self.tail = None
        elif not self.head.next.next:
            self.tail.prev = None
            self.head = self.tail
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_last(self):
        if not self.tail:
            print(f"Cписок порожній!")
        elif not self.tail.prev:
            self.tail = None
            self.head = None
        elif not self.tail.prev.prev:
            self.head.next = None
            self.tail = self.head
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def remove_by_value(self, data):
        if not self.head:
            print(f"Cписок порожній!")
        elif not self.head.next:
            if data == self.head.data:
                self.head = None
                self.tail = None
            else:
                print(f"Значення {data} немає у списку!")
        else:
            if data == self.head.data:
                self.remove_first()
                return
            elif data == self.tail.data:
                self.remove_last()
                return
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    current.next.prev = current
                    return
                current = current.next
            print(f"Значення {data} немає у списку!")

    def remove_at(self, index):
        if not self.head:
            print(f"Cписок порожній!")
        elif not self.head.next:
            if index == 0:
                self.head = None
                self.tail = None
            else:
                print(f"Индек {index} великий для списку!")
        else:
            if index == 0:
                self.remove_first()
                return
            current = self.head
            count = 1
            while current.next.next:
                if count == index:
                    current.next = current.next.next
                    current.next.prev = current
                    return
                current = current.next; count += 1
            if count == index:
                self.remove_last()
                return
            print(f"Индек {index} великий для списку!")

    def remove_repeat(self):
        if not self.head:
            print(f"Cписок порожній!")
        else:
            current = self.head
            repeat = [current.data]
            while current.next.next:
                if current.next.data not in repeat:
                    repeat.append(current.next.data)
                    current = current.next
                else:
                    current.next = current.next.next
                    current.next.prev = current
    
    ###################################_GET_METODS_###################################

    def get_first(self):
        if self.head:
            return self.head.data
        print(f"Cписок порожній!")
    
    def get_last(self):
        if self.tail:
            return self.tail.data
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
            head = self.head
            tail = self.tail
            while head:
                if data == head.data: 
                    return True
                if data == tail.data: 
                    return True
                head = head.next
                tail = tail.prev
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



if __name__ == "__main__":
    Linked = DoublyLinkedList()
    
    # Додавання елементів у список:
    Linked.prepend(1)   # add 1
    Linked.prepend(0)   # add 0
    Linked.append(2)    # add 2
    Linked.append(3)    # add 3
    Linked.insert_after(3, 4)   # add 4
    Linked.insert_after(4, 5)   # add 5
    Linked.insert_at(6, 6)  # add 6
    Linked.insert_at(7, 7)  # add 7
    print("Додавання елементів у список:", Linked, '\n')

    # Видалення елементів зі списку:
    Linked.remove_first()   # del 0
    Linked.remove_last()    # del 7
    Linked.remove_by_value(2)   # del 2
    Linked.remove_at(1)     # del 3
    print("Видалення елементів зі списку:", Linked, '\n')

    Linked.insert_at(0, 0)  # add 0
    Linked.insert_at(2, 0)  # add 0
    Linked.insert_at(4, 0)  # add 0
    Linked.insert_at(6, 0)  # add 0
    Linked.remove_repeat()  # del repeat     # Після цих двух оперцій список
    Linked.remove_by_value(0)    # del 0     # 100% не має 0, а також повтр.
    print("Видалення елементів зі списку:", Linked, '\n')

    # Отримання елемента зі списку:
    print("Отримання елемента зі списку:", end=' ')
    print(Linked.get_first(), end=', ')
    print(Linked.get_at(1),   end=', ')
    print(Linked.get_at(2),   end=', ')
    print(Linked.get_last())
    print()

    # Зміна значення елемента:
    Linked.set_at(0, 0)
    Linked.set_at(1, 1)
    Linked.set_at(2, 2)
    Linked.set_at(3, 3)
    print("Зміна значення елемента:", Linked)

    Linked.set_by_value(0, 3)   # Хотів розвернути список, а
    Linked.set_by_value(1, 2)   # вийлшо що я змінити усі
    Linked.set_by_value(2, 3)   # значення на 0
    Linked.set_by_value(3, 0)   # ха-ха-ха-ха затупок
    print("Зміна значення елемента:", Linked, '\n')

    # Получение даних:
    print("Получение даних:")
    print(Linked.contains(0))
    print(Linked.contains(1))
    print()

    print("Получение довжини:")
    print('length ->', Linked.length())
    Linked.remove_repeat()
    print('length ->', Linked.length())
    print()

    # Перевірка коректності списку: 
    print("Перевірка коректності списку: \n   Від верху до низу:", end=' ')
    current = Linked.head   
    while current: 
        print(current.data, end=', ')
        current = current.next
    print("\n   Від низу до верху:", end=' ')

    current = Linked.tail
    while current: 
        print(current.data, end=', ')
        current = current.prev
    print("\n\nПеревірка кінціво на None:")

    if Linked.head:
        print('  ', Linked.head.prev, Linked.tail.next)