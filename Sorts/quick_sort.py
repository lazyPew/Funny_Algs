from random import randint, choice

def quick(array):
    if len(array) <= 1:
        return array
    else:
        left, right = [], []
        i = randint(0,len(array)-1)
        for j in array:
            if j < array[i]:
                left.append(j)
            else:
                right.append(j)
        return quick(left) + quick(right)


# ar=nrand.randint(0,100,4)
ar = [randint(0, 100) for _ in range(8)]
print(ar)
print(quick(ar))