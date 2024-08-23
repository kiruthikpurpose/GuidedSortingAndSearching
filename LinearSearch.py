def linear_search(arr, target):
    # Traverse through all elements in the array
    for i in range(len(arr)):
        # If the target is found, return the index
        if arr[i] == target:
            return i
    # If the target is not found, return -1
    return -1

# Example usage
arr = [2, 4, 0, 1, 9]
target = 1
result = linear_search(arr, target)
print("Element found at index:", result)
