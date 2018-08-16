# Bubble sort

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr

# test

lst = [4, 9, 7, 1, 3, 6, 5]

print(bubble_sort(lst))
