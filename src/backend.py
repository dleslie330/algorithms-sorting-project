import random
from time import time
import timeit
from typing import Callable, Tuple

MIN_RANDOM_VALUE_RANGE = 1
MAX_RANDOM_VALUE_RANGE = 1000000000
DEFAULT_ARRAY_SIZE = 8


def pancake_sort(arr: list[int]) -> list[int]:
    """
    pancake_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """

    if len(arr) <= 1:
        return arr

    for size in range(len(arr), 1, -1):
        maxindex = max(range(size), key=arr.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                arr[:maxindex+1] = reversed(arr[:maxindex+1])
            # Flip it into its final position
            arr[:size] = reversed(arr[:size])
    return arr
# https://rosettacode.org/wiki/Sorting_algorithms/Pancake_sort#Python

def bubble_sort(arr: list[int]) -> list[int]:
    """
    bubble_sort _summary_

    Args:
        arr (list[int]): _description_

    Returns:
        list[int]: _description_
    """

    changed = True
    while changed:
        changed = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                changed = True
    return arr
# https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort#Python

def quick_sort(arr: list[int]) -> list[int]:
    """
    quick_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """

    return (quick_sort([y for y in arr[1:] if y <  arr[0]]) + 
            arr[:1] + 
            quick_sort([y for y in arr[1:] if y >= arr[0]])) if len(arr) > 1 else arr
# https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def merge_sort(arr: list[int]) -> list[int]:
    """
    merge_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """
    if len(arr) <= 1:
        return arr
 
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
# https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(__merge(left, right))
# https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python


def time_sorting_fn(sorting_fn: Callable[[list[int]], list[int]], arr: list[int], repeat: int = 1000) -> int:
    """
    time_sort takes a function and an array and returns how long it took
    for that array to be sorted

    Args:
        sorting_fn (Callable[[list[int]], list[int]]): sorting function to use
        arr (list[int]): array to sort

    Returns:
        int: amount of time it took to sort
    """
    return timeit.timeit(lambda: sorting_fn(arr), number=repeat)


def create_sorted_array_with_one_mistake(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    """
    create_sorted_array_with_one_swap makes an array that only has one value out of place
    example: [1, 2, 7, 3, 4]
    in this case, 7 is out of place, but moving it to the end of the array will 
    easily sort the array
    TODO Make methods similar to this but they have smaller elements or something
    TODO Code review

    Args:
        size (int, optional): size of the array . Defaults to DEFAULT_ARRAY_SIZE.

    Returns:
        list[int]: _description_
    """
    sorted_array = sorted(create_random_array())
    (pos_to_grab, pos_to_insert_into) = random.sample(
        range(0, len(sorted_array)), 2)
    grabbed_elem = sorted_array.pop(pos_to_grab)
    sorted_array.insert(pos_to_insert_into, grabbed_elem)
    return sorted_array


def create_reversed_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    """
    create_reversed_array creates a list of numbers that is sorted in descending order

    Args:
        size (int): size of the array

    Returns:
        list[int]: sorted array
    """
    return list(reversed(sorted(create_random_array(size))))


def create_sorted_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return list(sorted(create_random_array(size)))


def create_array_of_one_value(size: int = DEFAULT_ARRAY_SIZE, single_value: int = random.random()) -> list[int]:
    return [single_value] * size


def create_random_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return random.sample(range(MIN_RANDOM_VALUE_RANGE, MAX_RANDOM_VALUE_RANGE), size)

# TODO Think of more cases that we should look for when sorting arrays
