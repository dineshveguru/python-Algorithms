a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
k = int(input())


def search(arr, element):
    mid = len(arr) // 2
    if element > arr[mid]:
        arr = arr[:mid]
        search(arr, element)
    elif element < arr[mid]:
        arr = arr[mid:]
        search(arr, element)
    elif element == arr[mid]:
        print(f"element found at {mid+1}")
    elif element != arr[mid]:
        print("element doesnot found in array")


search(a, k)