import random
import time

from bubble_sort import bubble_sort
from quick_sort import quick_sort


sizes = [1000, 5000, 10000, 50000]


def generate_array(n):

    arr = []

    for i in range(n):

        number = random.randint(0, 100000)

        arr.append(number)

    return arr


def test_algorithm(func, data):

    start = time.time()

    func(data)

    end = time.time()

    return end - start


for size in sizes:

    data = generate_array(size)

    # копии массива
    data1 = data.copy()
    data2 = data.copy()

    bubble_time = test_algorithm(bubble_sort, data1)

    quick_time = test_algorithm(quick_sort, data2)

    print("Размер массива:", size)
    print("Bubble Sort время:", bubble_time)
    print("Quick Sort время:", quick_time)
    print()