def sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        sort(l)
        sort(r)
        merge(l, r, arr)
    return arr


def merge(left, right, result):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left[i]
            i = i + 1
            k = k + 1
        else:
            result[k] = right[j]
            k = k + 1
            j = j + 1
    while i < len(left):
        result[k] = left[i]
        k = k + 1
        i = i + 1
    while j < len(right):
        result[k] = right[j]
        k = k + 1
        j = j + 1
    return result


a = []
n = int(input("enter how many elements : "))
for i in range(n):
    a.append(int(input(f"enter {i+1} element : ")))

print("array before sorting >")
print(a)
sort(a)
print("array after sorting >")
print(a)




