a = [1, 1, 1, 8, 2]


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


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
    quicksort(start, boundary - 1, arr)
    quicksort(boundary + 1, end, arr)


quicksort(0, len(a) - 1, a)
print(a)