# №8 Поразрядная

def bucket_sort_by_digit(array, exponent):
    out = []
    buckets = [[] for _ in range(10)]

    for item in array:
        digit = (item // exponent) % 10
        buckets[digit].append(item)

    for bucket in buckets:
        for item in bucket:
            out.append(item)
    
    return out


def radix_sort(arr):
    if not arr:
        return arr
        
    max_element = max(arr)
    exponent = 1
    
    while max_element // exponent > 0:
        
        arr = bucket_sort_by_digit(arr, exponent)
        
        exponent *= 10
        
    return arr


print(radix_sort([12, 4, 890, 23, 1, 7, 2]))
