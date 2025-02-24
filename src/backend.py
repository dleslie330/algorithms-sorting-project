from typing import Callable

# random.sample(range(10, 30), 5)
MIN_RANDOM_VALUE_RANGE = -1
MAX_RANDOM_VALUE_RANGE = -1
DEFAULT_ARRAY_SIZE = -1

def pancake_sort(arr: list[int]) -> list[int]:
    """
    pancake_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """
    return []

def bubble_sort(arr: list[int]) -> list[int]:
    """
    bubble_sort _summary_

    Args:
        arr (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    return []

def quick_sort(arr: list[int]) -> list[int]:
    """
    quick_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """
    return []

def merge_sort(arr: list[int]) -> list[int]:
    """
    merge_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """
    return []

def time_sort(sorting_fn: Callable[[list[int]], list[int]], arr: list[int]) -> int:
    """
    time_sort takes a function and an array and returns how long it took
    for that array to be sorted

    Args:
        sorting_fn (Callable[[list[int]], list[int]]): sorting function to use
        arr (list[int]): array to sort

    Returns:
        int: amount of time it took to sort
    """
    
    return -1

def create_sorted_array_with_one_mistake(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    """
    create_sorted_array_with_one_swap makes an array that only has one value out of place
    example: [1, 2, 7, 3, 4]
    in this case, 7 is out of place, but moving it to the end of the array will 
    easily sort the array
    TODO Make methods similar to this but they have smaller elements or something

    Args:
        size (int, optional): size of the array . Defaults to DEFAULT_ARRAY_SIZE.

    Returns:
        list[int]: _description_
    """
    return []

def create_reversed_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    """
    create_reversed_array creates a list of numbers that is sorted in descending order

    Args:
        size (int): size of the array

    Returns:
        list[int]: sorted array
    """
    return []
 
def create_sorted_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return []

def create_array_of_one_value(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return []

def create_random_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return []

# TODO Think of more cases that we should look for when sorting arrays