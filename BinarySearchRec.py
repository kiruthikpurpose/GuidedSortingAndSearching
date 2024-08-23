def binary_search_recursive(arr, target, left, right):
    # Base case: If the left index exceeds the right, the target is not present
    if left > right:
        return -1
    
    # Find the middle index
    mid = (left + right) // 2
    
    # Check if the target is present at the middle index
    if arr[mid] == target:
        return mid
    
    # If the target is smaller than mid, it can only be present in the left subarray
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Otherwise, the target can only be present in the right subarray
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
# Call the function with initial left and right indices
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print("Element found at index:", result)
