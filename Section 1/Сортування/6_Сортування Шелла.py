from random import randint

def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position]=currentvalue

if __name__ == "__main__":
    print(arr := [randint(1,20) for _ in range(10)])
    shellSort(arr)
    print(arr)
    
    # Супере перевірка на 100 повторів:
    for i in range(100):
        arr = [randint(1,20) for _ in range(10)]
        copy = arr.copy()
        shellSort(arr)
        if not arr == sorted(copy): print(False); break
        else: print(True, end=' ')