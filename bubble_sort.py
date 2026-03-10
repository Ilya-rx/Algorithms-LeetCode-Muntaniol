# пузырьковая сортировка


def bubble_sort(arr):

    n = len(arr)

    # внешний цикл
    for i in range(n):

        # внутренний цикл
        for j in range(n - 1):

            if arr[j] > arr[j + 1]:

                # меняем местами
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr