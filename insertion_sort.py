def insertion_sort(arr):
    comparisons = 0
    assignments = 0
    for j in range(1, len(arr)):
        key = arr[j]
        assignments += 1
        i = j - 1
        while i >= 0 and arr[i] > key:
            comparisons += 1
            arr[i + 1] = arr[i]
            assignments += 1
            i -= 1
        if i >= 0:
            comparisons += 1
        arr[i + 1] = key
        assignments += 1
    return arr, comparisons, assignments

A = [53, 5, 44, 47, 35, 83, 82, 85, 28]
sorted_A, comp, assign = insertion_sort(A.copy())
print("Sorted array:", sorted_A)
print("Comparisons:", comp)
print("Assignments:", assign)

