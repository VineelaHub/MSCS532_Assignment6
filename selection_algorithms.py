"""
selection_algorithms.py

Implements two algorithms for selecting the k-th smallest element:
1. Deterministic Select using Median of Medians (worst-case O(n))
2. Randomized Quickselect (expected O(n))
"""

from __future__ import annotations

import random
from typing import List, Sequence, TypeVar

T = TypeVar("T")


class SelectionError(ValueError):
    """Raised when input to a selection algorithm is invalid."""

# Validation helpers

def _validate_input(arr: Sequence[T], k: int) -> None:
    """
    Validate common input rules.

    Parameters
    ----------
    arr : Sequence[T]
        Input sequence.
    k : int
        1-based order statistic to select.

    Raises
    ------
    SelectionError
        If the array is empty or k is out of range.
    TypeError
        If k is not an integer.
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer using 1-based indexing.")
    if len(arr) == 0:
        raise SelectionError("Input array must not be empty.")
    if k < 1 or k > len(arr):
        raise SelectionError(f"k must be between 1 and {len(arr)} inclusive.")


# Partition helper

def _three_way_partition(arr: Sequence[T], pivot: T) -> tuple[List[T], List[T], List[T]]:
    """
    Partition an array into elements less than, equal to, and greater than pivot.

    This makes the algorithms robust in the presence of duplicate values.
    """
    lows: List[T] = []
    equals: List[T] = []
    highs: List[T] = []

    for value in arr:
        if value < pivot:
            lows.append(value)
        elif value > pivot:
            highs.append(value)
        else:
            equals.append(value)

    return lows, equals, highs


# Deterministic Select: Median of Medians

def deterministic_select(arr: Sequence[T], k: int) -> T:
    """
    Return the k-th smallest element using the Median of Medians algorithm.

    Parameters
    ----------
    arr : Sequence[T]
        Input sequence of comparable values.
    k : int
        1-based index of the desired order statistic.

    Returns
    -------
    T
        The k-th smallest element.
    """
    _validate_input(arr, k)
    data = list(arr)
    return _deterministic_select_recursive(data, k)



def _deterministic_select_recursive(arr: List[T], k: int) -> T:
    """Recursive helper for deterministic select using 1-based k."""
    n = len(arr)

    # Small instance: sort directly.
    if n <= 5:
        return sorted(arr)[k - 1]

    # Step 1: divide into groups of 5.
    groups = [arr[i:i + 5] for i in range(0, n, 5)]

    # Step 2: find each group median.
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Step 3: recursively find median of medians.
    pivot = _deterministic_select_recursive(medians, (len(medians) + 1) // 2)

    # Step 4: partition around pivot.
    lows, equals, highs = _three_way_partition(arr, pivot)

    # Step 5: recurse into the appropriate side.
    if k <= len(lows):
        return _deterministic_select_recursive(lows, k)
    if k <= len(lows) + len(equals):
        return pivot
    return _deterministic_select_recursive(highs, k - len(lows) - len(equals))


# Randomized Quickselect

def randomized_select(arr: Sequence[T], k: int) -> T:
    """
    Return the k-th smallest element using randomized Quickselect.

    Parameters
    ----------
    arr : Sequence[T]
        Input sequence of comparable values.
    k : int
        1-based index of the desired order statistic.

    Returns
    -------
    T
        The k-th smallest element.

    """
    _validate_input(arr, k)
    data = list(arr)
    return _randomized_select_recursive(data, k)



def _randomized_select_recursive(arr: List[T], k: int) -> T:
    """Recursive helper for randomized quickselect using 1-based k."""
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows, equals, highs = _three_way_partition(arr, pivot)

    if k <= len(lows):
        return _randomized_select_recursive(lows, k)
    if k <= len(lows) + len(equals):
        return pivot
    return _randomized_select_recursive(highs, k - len(lows) - len(equals))


# Utility functions for testing/demo

def verify_selection_algorithms(arr: Sequence[T], k: int) -> dict[str, T]:
    """
    Run both algorithms and compare against Python's sorted result.
    """
    expected = sorted(arr)[k - 1]
    deterministic = deterministic_select(arr, k)
    randomized = randomized_select(arr, k)
    return {
        "expected": expected,
        "deterministic": deterministic,
        "randomized": randomized,
    }


if __name__ == "__main__":
    sample = [12, 3, 5, 7, 4, 19, 26, 3, 7, 1]
    k_value = 4

    print("Input array:", sample)
    print(f"{k_value}-th smallest using deterministic select:", deterministic_select(sample, k_value))
    print(f"{k_value}-th smallest using randomized select:", randomized_select(sample, k_value))
    print("Verification:", verify_selection_algorithms(sample, k_value))
