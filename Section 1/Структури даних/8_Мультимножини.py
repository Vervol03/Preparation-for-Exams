"""
 Мульти-множина (Multiset) це структура даних, яка подібна до множині, 
 але дозволяє зберігати не тільки унікальні елементи, але і допускає 
 повторювані елементи. 
 Вона може бути охарактеризована як колекція елементів, в якій кожен елемент 
 має пов'язане з ним число входжень, що його називають "мультиплісітетом".
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.next = None


class MultiSet:
    MAX_SIZE = 4

    def __init__(self):
        self.slots = [None] * MultiSet.MAX_SIZE

    @staticmethod
    def hash(key: int) -> int:
        return key % MultiSet.MAX_SIZE

    def add(self, value):
        hash_key = MultiSet.hash(value)
        slot = self.slots[hash_key]

        if slot is None:
            self.slots[hash_key] = Node(value)
        else:
            while slot:
                if slot.value == value:
                    slot.count += 1
                    return
                if slot.next is None:
                    break 
                slot = slot.next
            
            slot.next = Node(value)

    def remove(self, value):
        hash_key = MultiSet.hash(value)
        slot = self.slots[hash_key]
        prev = None
        while slot:
            if slot.value == value:
                if slot.count > 1:
                    slot.count -= 1
                else:
                    if prev:
                        prev.next = slot.next
                    else:
                        self.slots[hash_key] = slot.next
                return
            prev = slot
            slot = slot.next

    def count(self, value):
        hash_key = MultiSet.hash(value)
        slot = self.slots[hash_key]
        while slot:
            if slot.value == value:
                return slot.count
            slot = slot.next
        return 0

    def __repr__(self):
        elements = []
        for node in self.slots:
            if node:
                el = []
                while node:
                    el.append((node.value, node.count))
                    node = node.next 
                elements.append(el)
            else:
                elements.append(node)
        
        return "{\n  " + ", \n  ".join(str(elem) for elem in elements) + "\n}"
    


if __name__ == "__main__":
    hash_set = MultiSet()

    for i in range(65, 91): hash_set.add(i) 
    print(hash_set)

    hash_set.add(90)
    hash_set.add(90) 
    hash_set.add(90) 

    print("Кількість значень 90:", hash_set.count(90))

    for i in range(71, 91): hash_set.remove(i)
    print(hash_set)

    print("Кількість значень 90:", hash_set.count(90))