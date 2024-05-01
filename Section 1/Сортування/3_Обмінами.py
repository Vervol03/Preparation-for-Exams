"""
 Сортування за обміном (Bubble Sort):
    Ідея: Проходить по масиву багаторазово, порівнюючи і змінюючи місцями сусідні елементи до того часу, поки масив повністю відсортований. 
          На кожному проході найбільший (або маленький) елемент спливає в кінець (або початок) масиву. 
          У найгіршому випадку алгоритм має квадратичну тимчасову складність, що робить його неефективним для великих масивів даних.
    Переваги:
        Простий у реалізації.
        Добре працює на майже відсортованих масивах.
    Недоліки:
        Повільно працює на великих масивах.
        Неефективний на майже відсортованих масивах.
"""
from random import randint

def sort_by_exchanges(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < n-i-1:
            if arr[j] > arr[j+1]: 
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j += 1
        i += 1

if __name__ == "__main__":

    print(arr := [randint(1,20) for _ in range(10)])
    sort_by_exchanges(arr)
    print(arr)
    
    # Супере перевірка на 100 повторів:
    for i in range(100):
        arr = [randint(1,20) for _ in range(10)]
        copy = arr.copy()
        sort_by_exchanges(arr)
        if not arr == sorted(copy): print(False); break
        else: print(True, end=' ')