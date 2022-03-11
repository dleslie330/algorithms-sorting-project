from time import time
from backend import *
import random
import timeit
import pytest


def test_pancake_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == pancake_sort(arr)


def test_bubble_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == bubble_sort(arr)


def test_quick_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == quick_sort(arr)


def test_merge_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == merge_sort(arr)


def test_create_sorted_array():
    arr = create_sorted_array()
    assert sorted(arr) == arr
    failing_arr = [3, 4, 5, 12, 9]
    assert sorted(failing_arr) != failing_arr


def test_create_reversed_array():
    arr = create_reversed_array()
    assert sorted(arr) == list(reversed(arr))
    failing_arr = [3, 4, 8, 5]
    assert sorted(failing_arr) != list(reversed(failing_arr))


def test_create_array_of_one_value():
    arr = create_array_of_one_value()
    single_value = arr[0]
    assert all(map(lambda x: x == single_value, arr))


def test_create_sorted_array_with_one_mistake():
    arr = create_sorted_array_with_one_mistake()
    prev = arr[0]
    mistake_count = 0
    for x in arr:
        if x < prev:
            mistake_count += 1
        else:
            prev = x
    assert mistake_count == 1


def test_quick_sort_does_not_throw_stack_overflow():
    try:
        merge_sort(create_random_array(100000000))
    except MemoryError as e:
        pytest.fail(f'Memory Error has occurred')

# # @pytest.mark.repeat(20)
# def test_time_sort():
#     arr = create_random_array(3000)
#     returned_time_passed = time_sorting_fn(merge_sort, arr)
#     actual_time_passed = timeit.timeit(
#         lambda: time_sorting_fn(merge_sort, arr), number=1000)
#     assert actual_time_passed - returned_time_passed == pytest.approx(0, 1e-3)
