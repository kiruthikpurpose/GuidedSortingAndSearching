def binary_search(arr, target):
    # Sort the array before performing binary search
    arr.sort()
    left, right = 0, len(arr) - 1
    # Continue searching while the left index is less than or equal to the right index
    while left <= right:
        mid = (left + right) // 2
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    # If the element is not present, return -1
    return -1

# Example usage
arr = [2, 4, 0, 1, 9]
target = 4
result = binary_search(arr, target)
print("Element found at index:", result)
