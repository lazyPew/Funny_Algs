from random import randint

# ar=nrand.randint(0,100,4)
ar = [randint(0, 100) for _ in range(40)]
print(ar)

def merging(array):
    if len(array) > 1:
        m = len(array) // 2
        left = array[:m]
        right = array[m:]
        merging(left)
        merging(right)
        l = 0
        r = 0
        for k in range(len(left)+len(right)):
            if l < len(left) and r < len(right):
                if left[l] < right[r]:
                    array[k] = left[l]
                    l += 1
                else:
                    array[k] = right[r]
                    r += 1
            elif l < len(left):
                array[k] = left[l]
                l += 1
            elif r < len(right):
                array[k] = right[r]
                r += 1
    return array

print(merging(ar))