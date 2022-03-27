a = [1, 2, 3, 4]


def search(arr, element):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            left = mid + 1
        elif arr[mid] > element:
            right = mid - 1
    else:
        return -1


index = search(a, 2)
if index == -1:
    print("element not found in array")
else:
    print(f"element found at {index}")