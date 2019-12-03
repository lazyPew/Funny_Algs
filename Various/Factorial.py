def factory(n):
    res = 1
    if n >= 2:
        for i in range(1,n+1):
            res *= i
    return res

fact =  input('Input wanted factorial:')
print(factory(int(fact)))