def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]      # Element to be inserted
        j = i - 1
        
        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place key at correct position
    
    return arr


# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
