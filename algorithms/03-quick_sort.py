"""Quick sort algorythm choses a pivot element (randomly or manualy).
    All elements less than pivot move to the left, the ones that are more
    than pivot - to the right. Then algorythm uses recursion to both of
    pivot sides."""

def quick_sort(arr):
    '''Quick sort algorythm. It takes from O(nlogn) to O(n*n) time.
    It depends on how successfully the pivot is chosen. Here we
    chose it manualy.'''
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr [1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([1, 15, 5, 18, 9, 10, 4]))                   # [1, 4, 5, 9, 10, 15, 18]
