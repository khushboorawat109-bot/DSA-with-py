def Divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = Divide(arr[:mid])
    right_half = Divide(arr[mid:])
    return Merge(left_half, right_half)
arr=[64,34,25,45,40,51,2]
def Merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged    

print(Divide(arr))