import random

# функция разделения массива
def partition(arr, low, high):
    # берем последний элемент как pivot
    pivot = arr[high]

    i = low - 1  # индекс для меньшего элемента

    # проходим по массиву
    for j in range(low, high):
        # если элемент меньше pivot
        if arr[j] <= pivot:
            i = i + 1

            # меняем элементы местами
            arr[i], arr[j] = arr[j], arr[i]

    # ставим pivot на правильное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # возвращаем позицию pivot
    return i + 1


def quick_sort(arr, low, high):

    # если в массиве больше одного элемента
    if low < high:

        # выбираем случайный pivot
        random_index = random.randint(low, high)

        # меняем его с последним элементом
        arr[random_index], arr[high] = arr[high], arr[random_index]

        # разделяем массив
        pi = partition(arr, low, high)

        # сортируем левую часть
        quick_sort(arr, low, pi - 1)

        # сортируем правую часть
        quick_sort(arr, pi + 1, high)


# пример
arr = [8, 3, 5, 2, 9, 1]

quick_sort(arr, 0, len(arr) - 1)

print("Отсортированный массив:", arr)