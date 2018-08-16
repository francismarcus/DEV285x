# Linear search

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return f"{target} found at index: {i}"
    return -1

# test

lst = ["dog", "cat", "bird"]

print(linear_search(lst, "cat"))