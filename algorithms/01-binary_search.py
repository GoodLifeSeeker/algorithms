def binary_search(some_list, item):
    '''Func looks for item in some_list. It takes O(logn) time.
    It works only if the list is sorted. It returns index of element.'''

    low = 0
    high = len(some_list) - 1

    while low <= high:
        mid = int((low + high)//2)
        guess = some_list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# binary search checking
a = [1, 3, 4, 5, 11, 15, 22, 28, 31, 32, 33, 34, 35, 60, 96, 99, 102, 203, 315]
        
print(binary_search(a, b:=28))   # 7
print(binary_search(a, b:=156))  # None
print(binary_search(a, b:=1))    # 0
