# Binary search

def binary_search(arr, target):
    mid = len(arr) // 2

    if arr[mid] == target:
        return f"Found {target}."

    elif len(arr) == 1:
        return "Not found."

    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid:], target)

# test

lst = [1, 3, 4, 5, 6, 7, 9]

print(binary_search(lst, 7))