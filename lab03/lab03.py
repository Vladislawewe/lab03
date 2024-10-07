def bubble_sort(arr, ascending=True):
    """Сортировка массива arr методом пузырька."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ascending:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Ввод количества чисел
n = int(input("Введите количество чисел: "))

# Ввод чисел
numbers = []
print("Введите числа по одному:")
for i in range(n):
    numbers.append(int(input()))

# Запрос направления сортировки
direction = input("Введите направление сортировки (введите 'a' для возрастания, 'd' для убывания): ")
ascending = direction.lower() == 'a'

# Сортировка методом пузырька
bubble_sort(numbers, ascending)

# Вывод отсортированных чисел
print("Отсортированные числа:", numbers)
