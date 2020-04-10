import random

def compare(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def functional_quicksort(self, nums, compare_func):
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)
    lt = [v for v in nums if compare_func(v, pivot) < 0]
    eq = [v for v in nums if compare_func(v, pivot) == 0]
    gt = [v for v in nums if compare_func(v, pivot) > 0]

    return self.quicksort(lt) + eq + self.quicksort(gt)

"""
In place quick sort
"""
def sub_partition(array, start, end, idx_pivot, compare_func):

    'returns the position where the pivot winds up'

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if compare_func(array[j], pivot) <= 0:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def quicksort(array, compare_func, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot, compare_func)
    #print array, i, idx_pivot
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)