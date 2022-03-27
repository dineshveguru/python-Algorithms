a = [1, 2, 3, 4]
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# k = int(input())


def search(arr, element, left, right):
    if right < left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == element:
        return mid
    elif element < arr[mid]:
        return search(arr, element, left, mid - 1)
    elif element > arr[mid]:
        return search(arr, element, mid + 1, right)


index = search(a, 8, 0, len(a) - 1)
if index == -1:
    print("element not found in array")
else:
    print(f"element found at {index}")
