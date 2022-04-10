import time
start = time.time()
wt = [10, 20, 30]
val = [60, 100, 120]
capacity = 50
new_array = list(map(lambda x, y: x / y, val, wt))
add_weight = 0
add_val = 0
while add_weight < capacity:
    max_element = max(new_array)
    max_element_index = new_array.index(max_element)
    if wt[max_element_index] > capacity - add_weight:
        wt_ratio = (capacity - add_weight) / wt[max_element_index]
        add_weight += wt[max_element_index] * wt_ratio
        add_val += val[max_element_index] * wt_ratio
    else:
        add_weight += wt[max_element_index]
        add_val += val[max_element_index]
    new_array.pop(max_element_index)
    wt.pop(max_element_index)
    val.pop(max_element_index)
print(add_val)
stop = time.time()
print(f"time required : {stop - start}")