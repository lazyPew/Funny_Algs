from random import randint, choice

ar = [randint(0, 100) for _ in range(20)]
ar.sort()
print(ar)
N = choice(ar) # проверить работу при наличии искомого числа в массиве
# N = randint(0, 100) # проверить работу при отсутсвии искомого в массиве
print(N)

def bin_search(array,n):
    left, right = 0, len(array) - 1
    while left<=right:
        mid = (left + right) // 2
        print ('left = ', left, ' right = ', right)
        if n > array[mid]:
            left = mid + 1
        elif n < array[mid]:
            right = mid - 1
        elif n == array[mid]:
            print(True)
            return mid
    # if n == array[]
    return False

print(bin_search(ar,N))