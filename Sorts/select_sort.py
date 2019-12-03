import numpy.random as nrand

def selection(array):
    for i in range(len(array)):
        min = array[i]
        for j in range(i+1,len(array)):
            if array[j]<min:
                min = array[j]
                min_index = j
        if array[min_index]<array[i]:
            array[min_index], array[i] = array[i],array[min_index]
    return array

ar=nrand.randint(0,100,40)
nrand.shuffle(ar)
ar=selection(ar)
print(ar)