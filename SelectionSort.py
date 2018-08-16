# Selection sort

def selection(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

# test

lst = [4, 9, 7, 1, 3, 6, 5]

print(selection(lst))
