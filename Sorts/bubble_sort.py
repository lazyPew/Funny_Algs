import numpy.random as nrand

def bubble(array):
    for a in range(len(array)):
        b=0
        while (b<len(array)-1):
            if array[b]>array[b+1]:
                array[b],array[b+1]=array[b+1],array[b]
            b+=1
    return array

ar=nrand.uniform(0,100,40)
nrand.shuffle(ar)
ar=bubble(ar)
print(ar)