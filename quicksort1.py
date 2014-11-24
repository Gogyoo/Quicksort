""" Taking http://www.algorithmist.com/index.php/Quicksort as a guide,
this is an attempt to implement a quicksort algorithm."""

from random import randint

sample = 100 #replace with a user input if algo works fine
isample = sample - 1

def jumbled_list (n):
#creates a list with n RGNs. About 18 s for a million integers.
    jumbled = []
    for item in range(n):
        jumbled.append(randint(1,n))
    print jumbled
    return jumbled
    
jumbled = jumbled_list(sample)

def partition (array, low, high):
    pivot = array[-1]
    lw = 0
    for i in range (0, high-1):#, high) to be tried
        if array[i] < pivot:
            lw += 1
            array[i], array[lw] = array[lw], array[i]
        pivot, array[lw+1] = array[lw+1], pivot
        return lw+1
        
def quicksort (A, low, high):
    if low < high:
        p = partition (A, low, high)
        newlow = p + 1
        newhigh = p - 1
        quicksort(A, low, newhigh)
        quicksort(A, newlow, high)
        print A

quicksort (jumbled, 0, isample)
