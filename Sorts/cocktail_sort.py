from random import randint

def cocktail(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1
        for j in range(right, left, -1):
            if array[j] < array[j-1]:
                array[j], array[j - 1] = array[j - 1], array[j]
        left += 1
ar = [randint(0, 100) for _ in range(20)]
cocktail(ar)
