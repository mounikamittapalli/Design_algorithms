import random
import matplotlib.pyplot as plt
import timeit
import numpy as np
from bubble_sort import *
from selection_sort import *
from insertion_sort import *

def generate_random_array(size):
    # Generate a random array of integers for a given size
    return [random.randint(0, 99999) for i in range(size)]


# Benchmarking function for individual sorting algorithms
def calculate_benchmark_algorithm(number_of_runs):
    sizes = []
    insertion_times = []
    bubble_sort_times = []
    selection_sort_times = []
    for i in range(number_of_runs):
        # Generate a random array with a random size
        size = random.randint(10, 99999)  # Random size between 100 and 15000, we can change the numbers as needed
        arr = generate_random_array(size)  # Generate an array of the randomly generated size
        # print("Generated array: of size: ", arr, size)
        bubblesort_execution_time = timeit.timeit(lambda: bubble_sort(arr.copy()), number=1)
        selection_sort_execution_time = timeit.timeit(lambda: selection_sort(arr.copy()), number=1)
        insertion_sort_execution_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)

        #To verify if each of the algo is sorting the array correctly, uncomment the following code
        # bubble_sortedArr = bubble_sort(arr.copy())
        # insertion_sortedArr = insertion_sort(arr.copy())
        # selection_sortedArr = selection_sort(arr.copy())
        # print("Sorted array using the algorithms bubble: insertion: selection: ", bubble_sortedArr,insertion_sortedArr,selection_sortedArr)

        # print(f"time taken for Bubble sort {bubblesort_execution_time}, "
        #       f" for insertion sort: {insertion_sort_execution_time} "
        #       f" for selection sort: {selection_sort_execution_time}"
        #       f" for original array {arr} of size {size}")
        sizes.append(size)

        bubble_sort_times.append(bubblesort_execution_time)
        selection_sort_times.append(selection_sort_execution_time)
        insertion_times.append(insertion_sort_execution_time)

    return sizes, bubble_sort_times, selection_sort_times, insertion_times


# Number of different input sizes to test
number_of_runs = 20 # You can change this to test more random number of times
time_for_diff_sorting_algos = calculate_benchmark_algorithm(number_of_runs)

# print(f"Sizes and times before sorting: {time_for_diff_sorting_algos}")
# Sort the data based on input sizes for better line plotting
sorted_indices = np.argsort(time_for_diff_sorting_algos[0])  # Sort based on sizes
sizes_sorted = np.array(time_for_diff_sorting_algos[0])[sorted_indices]
bubble_sort_sorted = np.array(time_for_diff_sorting_algos[1])[sorted_indices]
selection_sort_sorted = np.array(time_for_diff_sorting_algos[2])[sorted_indices]
insertion_sort_sorted = np.array(time_for_diff_sorting_algos[3])[sorted_indices]
# print(f"Sizes and times after sorting:{sizes_sorted}, {bubble_sort_sorted}, {selection_sort_sorted}, {insertion_sort_sorted}")
# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes_sorted, bubble_sort_sorted, label="Bubble Sort", marker='x')
plt.plot(sizes_sorted, selection_sort_sorted, label="Selection Sort", marker='o')
plt.plot(sizes_sorted, insertion_sort_sorted, label="Insertion Sort", marker='^')
plt.xlabel('Random input sizes')
plt.ylabel('Time (seconds)')
plt.title('Benchmarking Sorting Algorithms with Random Input Sizes')
plt.legend()
plt.grid(True)
plt.show()
