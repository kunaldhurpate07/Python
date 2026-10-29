def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)

        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    left = [0] * n1
    right = [0] * n2

    # Copy elements into left array
    for i in range(n1):
        left[i] = arr[start + i]

    # Copy elements into right array
    for j in range(n2):
        right[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = start

    # Compare and merge
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements from left
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


# Main
arr = [4, 1, 3, 9, 7]

merge_sort(arr, 0, len(arr) - 1)

print(arr)