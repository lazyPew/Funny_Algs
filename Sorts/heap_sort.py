from random import randint

def heapify(array, length, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if (left < length) and array[left] > array[largest]:
        largest = left
    if (right < length) and array[right] > array[largest]:
        largest = right
    if largest != root:
        array[largest], array[root] = array[root], array[largest]
        heapify(array, length, largest)

def heap(array):
    for i in range(len(array) // 2, -1, -1):
        heapify(array, len(array),i)
    for j in range(len(array) - 1, 0, -1):
        array[j], array[0] = array[0], array[j]
        heapify(array, j, 0)
ar = [randint(0, 100) for _ in range(20)]
heap(ar)
print(ar)