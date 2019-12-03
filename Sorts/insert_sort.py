import numpy.random as nrand

def insertion(array):
    for m in range(1,len(array)):
        runner = array[m]
        n=m-1
        while(n>=0 and array[n] > runner):
            array[n+1], array[n] = array[n], array[n+1]
            n-=1
    return array

ar=nrand.randint(0,100,40)
nrand.shuffle(ar)
ar=insertion(ar)
print(ar)