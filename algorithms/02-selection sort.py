''' Selection sort finds the smallest element from given array and appends it to the new one.
It takes O(n*n) time in total.'''

def find_smallest(arr):
    '''Looks for the smallest elementof arr. It takes O(n) time.'''
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr):
    ''' Selection sort removes the smallest element from arr append it to 
    new_arr. It takes O(n) time.'''
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# Checking
a = [5, 22, 12, 1, 144, 39, 67, 55, 31, 8]
print(selection_sort(a))   # [1, 5, 8, 12, 22, 31, 39, 55, 67, 144]