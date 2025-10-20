def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
    return arr, comparisons, assignments

A = [53, 5, 44, 47, 35, 83, 82, 85, 28]
sorted_A, comp, assign = selection_sort(A.copy())
print("Sorted array:", sorted_A)
print("Comparisons:", comp)
print("Assignments:", assign)

