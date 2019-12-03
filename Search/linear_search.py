from random import randint, choice

ar = [randint(0, 100) for _ in range(30)]
ar.sort()
print(ar)
N = choice(ar) # проверить работу при наличии искомого числа в массиве
# N = randint(0, 100) # проверить работу при отсутсвии искомого в массиве
print(N)

def lin_search(array,n):
    for i in range(len(array)):
        if n == array[i]:
            return True, i
    return False

print(lin_search(ar,N))