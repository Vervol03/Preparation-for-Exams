"""
 Хеш-таблиця - це структура даних, яка використовує хеш-функцію для визначення 
 місця зберігання та швидкого пошуку даних у масиві чи таблиці. 
 Хеш-таблиці дозволяють виконувати операції додавання, пошуку та видалення 
 елементів у середньому за час O(1), що робить їх дуже ефективними для швидкого 
 доступу до даних.

 Колізія: Це ситуація, коли два або більше ключів мають однаковий хеш-код і, отже, 
 вказують на одне й те ж місце у масиві. Колізії виникають через обмежену 
 кількість можливих хеш-кодів у порівнянні з кількістю можливих ключів.

 У реалізації хеш-таблиці з ланцюжками, коли відбувається колізія, тобто коли два 
 ключі мають однаковий хеш, вони зберігаються в одному і тому ж слоті у вигляді ланцюжка 
 вузлів. Кожен вузол вказує на наступний вузол у ланцюжку, утворюючи послідовність.

 Детально ознайомитися: 3.1.3. Хешування та хеш-таблиці стр. 34-46.

 Як я зрозумів це словник однобічних списків, де списки вирішують проблему Колізії.
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Посилання на наступний вузол в ланцюжку


class HashTable:
    MAX_SIZE = 10  # Максимальний розмір хеш-таблиці

    def __init__(self):
        # Створення масиву слотів фіксованого розміру
        self.slots = [None] * HashTable.MAX_SIZE
    
    @staticmethod
    def hash(key: int) -> int:
        # Функція хешування: обчислює індекс слоту для заданого ключа
        return key % HashTable.MAX_SIZE
    
    def put(self, key, value):
        # Метод для додавання пари ключ-значення у хеш-таблицю
        hash_key = HashTable.hash(key)  # Обчислення індексу за наданим ключем
        slot = self.slots[hash_key]     # Отримання слоту за обчисленим індексом
        
        if slot: 
            # Якщо слот не порожній, перевіряємо, чи ключ вже присутній у ланцюжку
            while slot.next:
                if slot.key == key:  # Якщо ключ вже існує, замінюємо значення
                    slot.value = value
                    return
                slot = slot.next
            # Якщо ключ відсутній у ланцюжку, додаємо новий вузол у кінець
            slot.next = Node(key, value)
        else:
            # Якщо слот порожній, створюємо новий вузол
            self.slots[hash_key] = Node(key, value)

    def get(self, key):
        # Метод для отримання значення за ключем з хеш-таблиці
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]  # Отримання слоту за обчисленим індексом
        while slot:
            if slot.key == key:  # Якщо ключ співпадає, повертаємо відповідне значення
                return slot.value
            slot = slot.next # Перехід до наступного вузла у ланцюжку
        return None  # Якщо ключ не знайдено, повертаємо None

    def __repr__(self):
        # Метод для представлення хеш-таблиці у вигляді рядка
        elements = []
        for node in self.slots:
            if node:
                el = []
                while node:
                    el.append((node.key, node.value))   # Додаємо пару ключ-значення у список
                    node = node.next                    # Перехід до наступного вузла у ланцюжку
                elements.append(el)                     # Додаємо список у список елементів
            else:
                elements.append(node)  # Додаємо None у випадку порожнього слоту
        return str(elements)  # Повертаємо рядок із списком елементів


if __name__ == "__main__": # Приклад використання
    M = HashTable() 
    for i in range(65, 91): M.put(i, chr(i)) 
    for i in range(65, 91): print(M.get(i))

    M.put(65, "65") 
    print(M)