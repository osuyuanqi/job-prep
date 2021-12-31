# ******************************************
# 1. Bubble Sort: O(n^2)
# the largest element sink
# ******************************************

def bubSort(a):
    for i in range(len(a)):
        # a[len(a)-i -1] has been settled down after ith iteration
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        # print(a,a[len(a)-i -1])
    return a

# *******************************************
# 2. Selection Sort: O(n^2)
# the smallest element pop
# *******************************************

def selSort(a):
    for i in range(len(a)):
        i_min = i
        for j in range(i + 1 , len(a) ):
            # get the min_index
            if a[i_min] > a[j]:
                i_min = j
            # print(a)
        # smallest element is selected in the ith position per iteration
        a[i], a[i_min] = a[i_min], a[i]
    return a

# *******************************************
# 3. Insertion Sort: O(n^2)
# ith ele insert into the (0,ith) position
# *******************************************

def insSort(a):
    for i in range(len(a)):
        # compare the (i-1)th ele
        for j in range(0, i):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
            # print(a, i ,j, a[i],a[j])
    return a

# *******************************************
# 4.Merge Sort: O(nlogn)
# devide into pieces, compare and conquer
# *******************************************

def merSort(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    # merge function pick the first two orderly after iteration
    # e.g.if [3,2,1],then[3], [2][1]->merge([2],[1])->merge([3],[1][2])
    return merge(merSort(left),merSort(right))
def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # collect the largest remaining ele
    return result + left[i:] + right[j:]

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

# **********************************************************
# 5. Quick Sort:
# pick pivot, devide and conquer
# Note: faster than merge sort, win at pick pivot randomly
# **********************************************************

import random
def qsort(a):
    if len(a) < 2: 
        # single ele
        return a
    # random select after shuffle
    random.shuffle(a)
    pivot = a[0]
    left = [i for i in a if i < pivot]
    right = [i for i in a if i > pivot]
    return qsort(left) + [pivot] + qsort(right)
    

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

print(bubSort(numbers[::]))
print(selSort(numbers[::]))
print(insSort(numbers[::]))
print(merSort(numbers[::]))
print(qsort(numbers[::]))

