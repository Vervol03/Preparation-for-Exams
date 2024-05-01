"""
 Лінійний пошук: Пошук елемента у послідовності (наприклад, у масиві або 
                 списку) шляхом перевірки кожного елемента послідовно. 
                 Це простий, але неефективний метод, особливо для 
                 великих наборів даних.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    target = 7
    result = linear_search(arr, target)
    if result != -1:
        print(f"Елемент {target} знайдено в масиві на позиції {result}.")
    else:
        print(f"Елемент {target} не знайдено в масиві.")
