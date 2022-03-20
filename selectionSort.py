import time
a = [9, 8, 7]


# taken an initial array


begin = time.time()


def swap(arr, i, j):  # used for swapping two integers with their indexes in array
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


"""
iterating through the list and assuming
that the first indexed element is the
min element, and iterating through the array
again from the next element and finding the smallest 
element index and swap using swap function. 
"""

for i in range(len(a)):
    min_element_index = i
    for j in range(i + 1, len(a)):
        if a[j] <= a[min_element_index]:
            min_element_index = j
    swap(a, i, min_element_index)

print(a)

time.sleep(1)
end = time.time()
print(f"total time required : {end - begin - 1}")
