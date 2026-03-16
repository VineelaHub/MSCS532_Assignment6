"""
benchmark_selection.py

Empirically compares deterministic select (Median of Medians) and
randomized quickselect on different input sizes and distributions.

"""

from __future__ import annotations

import random
import statistics
import time
from typing import Callable, List

from selection_algorithms import deterministic_select, randomized_select


SelectionFunction = Callable[[List[int], int], int]



def generate_input(size: int, distribution: str) -> List[int]:
    """Generate test arrays for benchmarking."""
    if distribution == "random":
        return [random.randint(0, size * 10) for _ in range(size)]
    if distribution == "sorted":
        return list(range(size))
    if distribution == "reverse_sorted":
        return list(range(size, 0, -1))
    if distribution == "duplicates":
        return [random.randint(0, max(1, size // 10)) for _ in range(size)]
    raise ValueError(f"Unknown distribution: {distribution}")



def benchmark_algorithm(func: SelectionFunction, arr: List[int], k: int, trials: int = 5) -> float:
    """Return median runtime in milliseconds over multiple trials."""
    timings = []
    for _ in range(trials):
        data = arr[:]  # keep each trial independent
        start = time.perf_counter()
        result = func(data, k)
        end = time.perf_counter()

        # Safety check against Python's sorted result
        assert result == sorted(arr)[k - 1]
        timings.append((end - start) * 1000)

    return statistics.median(timings)



def run_benchmarks() -> None:
    sizes = [100, 500, 1000, 3000, 5000]
    distributions = ["random", "sorted", "reverse_sorted", "duplicates"]
    trials = 5

    print("Median runtime over", trials, "trials (milliseconds)")

    for distribution in distributions:
        print(f"\n=== Distribution: {distribution} ===")
        for size in sizes:
            arr = generate_input(size, distribution)
            k = size // 2 if size % 2 == 0 else (size + 1) // 2

            det_time = benchmark_algorithm(deterministic_select, arr, k, trials)
            rand_time = benchmark_algorithm(randomized_select, arr, k, trials)

            print(
                f"n={size:5d} | Deterministic: {det_time:10.3f} ms | "
                f"Randomized: {rand_time:10.3f} ms"
            )


if __name__ == "__main__":
    random.seed(42)
    run_benchmarks()
