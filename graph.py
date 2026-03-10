import matplotlib.pyplot as plt


sizes = [1000, 5000, 10000, 50000]

bubble_times = [0.05, 1.2, 4.8, 120]

quick_times = [0.002, 0.01, 0.03, 0.20]


plt.plot(sizes, bubble_times)
plt.plot(sizes, quick_times)

plt.xlabel("Размер массива")
plt.ylabel("Время")

plt.title("Сравнение алгоритмов")

plt.legend(["Bubble Sort", "Quick Sort"])

plt.show()