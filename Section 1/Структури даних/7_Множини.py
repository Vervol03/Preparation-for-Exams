"""
 Хеш-таблиця і Множини (Set) обидва є структури даних, які дозволяють швидко 
 виконувати операції додавання, видалення та перевірки наявності елементів. 
 
 Однак основна відмінність полягає в тому, що хеш-таблиця зберігає пари 
 ключ-значення, у той час як множина зберігає тільки унікальні елементи. 
 Таким чином, хеш-таблиця призначена для зберігання асоціативних даних, 
 а безліч – для роботи з унікальними елементами.

 Це як Сливник (Хеш-таблиця) але без ключа. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Set:
    MAX_SIZE = 5

    def __init__(self):
        self.slots = [None] * Set.MAX_SIZE

    @staticmethod
    def hash(key: int) -> int:
        return key % Set.MAX_SIZE

    def add(self, value):
        hash_key = Set.hash(value)
        slot = self.slots[hash_key]

        if slot is None:
            self.slots[hash_key] = Node(value)
        else:
            while slot:
                if slot.value == value: 
                    return
                if slot.next is None:
                    break
                slot = slot.next
            
            slot.next = Node(value)

    def contains(self, value):
        hash_key = Set.hash(value)
        slot = self.slots[hash_key]

        while slot:
            if slot.value == value:
                return True
            slot = slot.next

        return False

    def remove(self, value):
        hash_key = Set.hash(value)
        slot = self.slots[hash_key]

        prev = None
        while slot:
            if slot.value == value:
                if prev:
                    prev.next = slot.next
                else:
                    self.slots[hash_key] = slot.next
                return
            prev = slot
            slot = slot.next

    def __repr__(self):
        elements = []
        for node in self.slots:
            if node:
                el = []
                while node:
                    el.append(node.value)
                    node = node.next
                elements.append(el)
            else: elements.append(node)
        return "{\n  " + ", \n  ".join(str(elem) for elem in elements) + "\n}"


if __name__ == "__main__":

    hash_set = Set()

    for i in range(65, 91): hash_set.add(i) 
    print(hash_set)

    print(hash_set.contains(68), end=', ')
    print(hash_set.contains(75), end=', ')
    print(hash_set.contains(90))

    hash_set.add(90)
    hash_set.add(90) 
    hash_set.add(90) 

    for i in range(71, 91): hash_set.remove(i)
    print(hash_set)