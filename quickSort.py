def sort(arr, start, end):
    while start < end:
        boundary = partition(arr, start, end)
        sort(arr, start, boundary - 1)
        sort(arr, boundary + 1, end - 1)


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(arr, start, end):
    b = 0
    pivot = arr[end]
    for i in range(start, end + 1):
        if arr[i] <= pivot:
            swap(arr, i, b)
            b = b + 1
    return b - 1

a = [15, 6, 3, 1, 22, 10, 13]
print(sort(a, 0, len(a) - 1))