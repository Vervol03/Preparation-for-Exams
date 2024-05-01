"""
 Бінарний пошук: Це ефективний метод пошуку в упорядкованому масиві. Він швидко знаходить 
                 потрібний елемент, розділяючи пошуковий діапазон навпіл і порівнюючи шуканий 
                 елемент з елементом у середині. Використовується тільки для впорядкованих даних.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Елемент {target} знайдено в масиві на позиції {result}.")
    else:
        print(f"Елемент {target} не знайдено в масиві.")
