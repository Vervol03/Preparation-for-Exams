from random import randint

n = 20; d1 = []; d2 = []


# Звичайний спосіб 
def print_dupl(numbers):
    repeats = [False]*n
    for i in range(len(numbers)):
        if repeats[numbers[i]-1]: 
            d1.append(numbers[i])
        else: 
            repeats[numbers[i]-1] = True



# Бітовий спосіб вирішення задачі
def print_duplicates(numbers):
    repeats = [False]*(n//32+1)
    for i in range(len(numbers)):
        if is_SetBit(repeats, numbers[i]-1): 
            d2.append(numbers[i])
        else: 
            setBit(repeats, numbers[i]-1)

def is_SetBit(bitVector, index):
    row = getRow(index)
    col = getCol(index)
    return bitVector[row] & (1 << col) != 0

def setBit(bitVector, index):
    row = getRow(index)
    col = getCol(index)
    bitVector[row] |= 1 << col

def getRow(bit):
    return int(bit >> 5)

def getCol(bit): 
    return bit % 32


if __name__ == "__main__":
    numbers = [randint(0, n-1) for _ in range(n)]
    print_dupl(numbers); print_duplicates(numbers)
    # print(numbers); print(d1, d2) # Коли n <= 20 (> вже не зрозуміло)
    print(n-len(set(numbers)), '= Повторів у списку')
    print((len(d1)), '= Повторів звичайного способу')
    print((len(d2)), '= Повторів бітового способу')
