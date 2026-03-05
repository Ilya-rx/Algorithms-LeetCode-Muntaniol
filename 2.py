import random

# функция partition (та же самая, что использовали в QuickSort)
def partition(arr, low, high):

    pivot = arr[high]  # берем последний элемент как pivot
    i = low - 1

    for j in range(low, high):

        # если элемент меньше pivot
        if arr[j] <= pivot:
            i = i + 1

            # меняем элементы местами
            arr[i], arr[j] = arr[j], arr[i]

    # ставим pivot на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_select(arr, k):

    low = 0
    high = len(arr) - 1

    # продолжаем искать пока не найдем элемент
    while low <= high:

        # выбираем случайный pivot
        random_index = random.randint(low, high)

        # меняем его с последним элементом
        arr[random_index], arr[high] = arr[high], arr[random_index]

        # делаем разделение массива
        pi = partition(arr, low, high)

        # если позиция pivot совпадает с k
        if pi == k:
            return arr[pi]

        # если нужный элемент слева
        if k < pi:
            high = pi - 1

        # если нужный элемент справа
        else:
            low = pi + 1


# пример
arr = [7, 2, 9, 4, 1, 5, 3]

k = 3  # ищем 4-й наименьший элемент (индексация с 0)

result = quick_select(arr, k)

print("k-й наименьший элемент:", result)