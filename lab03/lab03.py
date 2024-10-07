def bubble_sort(arr):
 n = len(arr)
 for i in range(n - 1):
  for j in range(n - i - 1):
   if arr[j] > arr[j + 1]:
    arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ввод количества чисел
n = int(input("Введите количество чисел: "))

# Ввод чисел
numbers = []
print("Введите числа по одному:")
for i in range(n):
 numbers.append(int(input()))

# Сортировка методом пузырька
bubble_sort(numbers)

# Вывод отсортированных чисел
print("Отсортированные числа:", numbers)
