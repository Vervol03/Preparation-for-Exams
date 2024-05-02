from random import randint

def merge_sort(arr):
    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right, arr.copy())

def merge(left, right, merged):
    left_cursor  = 0
    right_cursor = 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


if __name__ == "__main__":

    print(arr := [randint(1,20) for _ in range(10)])
    print(merge_sort(arr))
    
    # Супере перевірка на 100 повторів:
    for i in range(100):
        arr = [randint(1,20) for _ in range(10)]
        copy = arr.copy()
        arr = merge_sort(arr)
        if not arr == sorted(copy): print(False); break
        else: print(True, end=' ')
