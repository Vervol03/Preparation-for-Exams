"""
 Сортування вставками (Insertion Sort):
    Ідея: На кожному кроці алгоритм бере один елемент із невідсортованої частини 
          масиву та вставляє його у правильне місце у відсортованій частині масиву. 
          Таким чином, відсортована частина масиву збільшується на один елемент на кожному кроці.
    Переваги:
        Простий у реалізації.
        Ефективний на невеликих чи частково відсортованих масивах.
    Недоліки:
        Повільно працює на великих масивах.
"""
from random import randint

def sort_by_inserts(arr):
    n = len(arr)
    i = 1
    while i < n:
        j = i
        while j > 0:
            if arr[j] < arr[j-1]: 
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j -= 1
            else: break
        i += 1

if __name__ == "__main__":

    print(arr := [randint(1,20) for _ in range(10)])
    sort_by_inserts(arr)
    print(arr)

    # Супере перевірка:
    for i in range(100):
        arr = [randint(1,20) for _ in range(10)]
        copy = arr.copy()
        sort_by_inserts(arr)
        if not arr == sorted(copy): print(False); break
        else: print(True, end=' ')