""" Taking http://www.algorithmist.com/index.php/Quicksort as a guide,
this is an attempt to implement a quicksort algorithm."""

from random import randint

sample = 100 #replace with a user input if algo works fine

def jumbled_list (n):
#creates a list with n RGNs. About 18 s for a million integers.
    jumbled = []
    for item in range(n):
        jumbled.append(randint(1,n))
    print jumbled
    return jumbled
    
jumbled_list(sample)

def partition (array, low, high):
    pivot = array[sample//2]
    leftwall = 1
    for i in range (0, high-1):#, high) to be tried
        if array[i] < pivot:
            leftwall += 1
            array[i], pivot = pivot, array[i]
        pivot, array[i] = array[i], pivot
        return pivot
        
def quicksort (A, low, high):
    if low < high:
        p = partition (A, low, high)
        quicksort(A, low, p - 1)
        quicksort(A, p + 1, high)
        print A

quicksort (jumbled_list, 0, sample - 1)
