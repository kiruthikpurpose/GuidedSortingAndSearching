def shell_sort(arr):
    # Start with a large gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Perform a gapped insertion sort for this gap size.
    while gap > 0:
        for i in range(gap, n):
            # Save the element at the current index
            temp = arr[i]
            
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Place temp (the original arr[i]) in its correct location
            arr[j] = temp
        
        # Reduce the gap for the next iteration
        gap //= 2

# Example usage
arr = [12, 34, 54, 2, 3]
print("Original array:", arr)
shell_sort(arr)
print("Sorted array:", arr)
