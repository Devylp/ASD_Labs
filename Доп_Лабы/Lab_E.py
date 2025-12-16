'''
E. Интересные пары
'''

n = int(input())
arr = [int(x) for x in input().split()]


def merge_sort_and_count(array):

    if len(array) <= 1:
        return array, 0
    
    mid = len(array) // 2
    
    left_piece, left_inv = merge_sort_and_count(array[:mid])
    right_piece, right_inv = merge_sort_and_count(array[mid:])
    
    merged_array, merge_inv = merge_and_count(left_piece, right_piece)
    
    return merged_array, left_inv + right_inv + merge_inv

def merge_and_count(a, b):
    result_merge = []
    i = j = 0
    count = 0

    while i < len(a) and j < len(b):
        
        if a[i] <= b[j]:
            result_merge.append(a[i])
            i += 1
        else:
            result_merge.append(b[j])
            j += 1
            count += (len(a) - i)

    if i < len(a):
        result_merge += a[i:]

    if j < len(b):
        result_merge += b[j:]
    
    return result_merge, count


_, result = merge_sort_and_count(arr)
print(result)