""" 
 Існують різні визначення алгоритму:
 Алгоритм — точний набір інструкцій (правил, процедур, команд), 
            які описують порядок дій певного виконавця для 
            розв’язання певної задачі чи певного класу задач 
            за скінченну кількість кроків. 

 Алгоритм — точний i зрозумілий опис послідовності дій над 
            заданими об’єктами, який після скінченної кількості 
            кроків приводить виконавця до досягнення вказаної 
            мети чи розв’язання поставленої задачі. 

 Алгоритм — будь-яка система об-числень, що виконуються за 
            строго певними правилами, яка після деякої 
            кількості кроків приводить до розв’язання 
            поставленої задачі. 

 Алгоритм — точне розпорядження, що визначає обчислювальний 
            процес, який іде від варійованих початкових 
            даних до шуканого результату.
"""

""""
 Найчастіше розглядають такі складності алгоритмів (від швидкого до повільного):
        O(1) — константна
    O(log n) — логарифмічна
        O(n) — лінійна
  O(n log n) — лінійно-логарифмічна
       O(n²) — квадратична
       O(n³) — кубічна
       O(n!) — факторіальна складність
"""

###########################################################

# Константна O(1)
def add(x, y):
    return x+y

# print(add(1, 2))

def print_pyramid():
    for i in range(5):
        print(" "*(5-i-1)+"*"*(2*i+1))

# print_pyramid()

###########################################################

# Логарифмічна O(log n) - Бінарний пошуку
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid+1
        else: right = mid-1
    
# print(binary_search([1, 3, 5, 13, 15, 17, 19], 17))

###########################################################

# Лінійна — O(n) - Пошуку максимального елемента
def find_max(arr):
    max_elem = arr[0]
    for num in arr:
        if num > max_elem: max_elem = num
    return max_elem

# print(find_max([3, 7, 2, 10, 5]))

###########################################################

# Лінійно-логарифмічна — O(n log n) - Швидке сортування
def quick_sort(arr):
    if len(arr) <= 1: return arr

    pivot  = arr[len(arr) // 2]
    left   = [x for x in arr if x  < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x  > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort([3, 6, 8, 10, 12, 2, 1]))


###########################################################

# Квадратична — O(n²) - Сортування вибором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# selection_sort([64, 25, 12, 22, 11])


###########################################################

# Кубічна — O(n³) - Перемноження двох матриць
def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

# print(matrix_multiply([[1,2],[3,4]], [[5,6],[7,8]]))

###########################################################

# Факторіальна — O(n!) - Всі перестановоки ел. у списку
def generate_permutations(arr):
    def backtrack(start):
        if start == len(arr):
            permutations.append(arr.copy())
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]
    
    permutations = []
    backtrack(0)
    return permutations

# print(len(generate_permutations([1, 2, 3, 4, 5])))



