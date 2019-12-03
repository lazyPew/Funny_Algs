from random import randint

def gnome(array):
    i = 1
    while i < len(array):
        if  array[i-1] <= array[i]:
            i += 1
        else:
            array[i-1], array[i] = array[i], array[i-1]
            if i > 1:
                i -= 1
ar = [randint(0, 100) for _ in range(20)]
gnome(ar)
print(ar)