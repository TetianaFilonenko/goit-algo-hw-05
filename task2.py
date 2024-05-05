def binary_search(arr, target):
    """
    Perform a binary search to find the upper bound of a target value in a sorted array.
    """
    low, high = 0, len(arr) - 1
    iterations = 0
    best_index = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            best_index = mid
            high = mid - 1

    if best_index is not None:
        return (iterations, arr[best_index])
    else:
        return (iterations, None)

# Example usage:
arr = [1.5, 2.3, 3.4, 4.7, 5.8, 6.2]
target = 4.0
result = binary_search(arr, target)
print("Iterations:", result[0], "Upper Bound:", result[1])
