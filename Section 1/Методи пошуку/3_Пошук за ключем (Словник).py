"""
 Пошук за ключем: Використовується в асоціативних структурах даних, таких 
                  як словники, хеш-таблиці тощо. Пошук відбувається за ключем, 
                  а не за позицією, що дозволяє швидко знаходити елемент за ключем.
 Ми вже його реалізовували коли створювали Словник (Хеш-таблицю).             
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None 

class HashTable:
    MAX_SIZE = 10

    def __init__(self):
        self.slots = [None] * HashTable.MAX_SIZE
    
    @staticmethod
    def hash(key: int) -> int:
        return key % HashTable.MAX_SIZE
    
    def put(self, key, value):
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]
        if slot: 
            while slot.next:
                if slot.key == key:
                    slot.value = value
                    return
                slot = slot.next
            slot.next = Node(key, value)
        else:
            self.slots[hash_key] = Node(key, value)

    def get(self, key):
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]
        while slot:
            if slot.key == key:
                return slot.value
            slot = slot.next
        return None


if __name__ == "__main__":

    hash_table = HashTable()

    hash_table.put(1, 'a')
    hash_table.put(2, 'b')
    hash_table.put(11, 'c')
    hash_table.put(12, 'd')

    print(hash_table.get(1))
    print(hash_table.get(2))
    print(hash_table.get(11))
    print(hash_table.get(12)) 
    print(hash_table.get(3)) 