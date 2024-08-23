def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array that will have sorted numbers according to the current digit
    count = [0] * 10  # Count array to store the count of occurrences of digits (0-9)

    # Store the count of occurrences of each digit in the current place value (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update the count array to have the actual position of the digits in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array back to arr, so that arr contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit (exp is 10^i where i is the current digit number)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)
