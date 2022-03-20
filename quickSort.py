a = [1, 1, 1, 8, 2]


# taken an initial array


def swap(arr, a, b):  # used for swapping two integers with their indexes in array
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


"""partioning the array such that the pivot element 
comes to its correct position in array and
all the elements less than pivot
comes to right side of pivot and 
all the elements greater than pivot comes to left side
of pivot"""


def partition(arr, start, end):
    b = start - 1
    pivot = arr[end]
    for i in range(start, end + 1):
        if arr[i] <= pivot:
            b += 1
            swap(arr, b, i)
    return b


def quicksort(start, end, arr):
    if start >= end:
        return
    boundary = partition(arr, start, end)
    quicksort(start, boundary - 1, arr)  # recursively calling the array and sorting the right part of pivot
    quicksort(boundary + 1, end, arr)  # recursively calling the array and sorting the left part of pivot


quicksort(0, len(a) - 1, a)
print(a)
