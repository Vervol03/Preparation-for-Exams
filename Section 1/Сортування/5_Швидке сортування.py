from random import randint

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_idx = partition(array, low, high)
        quick_sort(array, low, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, high)
    return array


if __name__ == "__main__":

    print(arr := [randint(1,20) for _ in range(10)])
    print(quick_sort(arr))
    
    # Супере перевірка на 100 повторів:
    for i in range(100):
        arr = [randint(1,20) for _ in range(10)]
        copy = arr.copy()
        arr = quick_sort(arr)
        if not arr == sorted(copy): print(False); break
        else: print(True, end=' ')
