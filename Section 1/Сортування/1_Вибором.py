"""
 Сортування вибором (Selection Sort):
    Ідея: На кожному кроці алгоритм знаходить мінімальний елемент невідсортованої частини 
          масиву та змінює його місцями з першим елементом невідсортованої частини. Після 
          цього межа відсортованої частини масиву зсувається на один елемент праворуч.
    Переваги:
         Простий у реалізації.
         Підходить для сортування невеликих масивів.
    Недоліки:
         Неефективний великих масивах.
         Нестійкий до нерівномірно розподілених даних.
"""
from random import randint

def sort_by_choice(arr):
    n = len(arr)
    i = 0
    while i < n-1:
        j = i
        index = i
        while j < n:
            if arr[j] < arr[index]: 
                index = j
            j += 1
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp
        i += 1

if __name__ == "__main__":
    print(arr := [randint(1,20) for _ in range(10)])
    sort_by_choice(arr)
    print(arr)
    # Супере перевірка:
    for i in range(100):
        arr = [randint(1,20) for _ in range(10)]
        copy = arr.copy()
        sort_by_choice(arr)
        if not arr == sorted(copy): print(False); break
        else: print(True, end=' ')