import random


# Заданные значения n для проведения экспериментов
n_nums = [100, 200, 500, 1000, 2000, 5000, 10000, 100000]


# Функция для вычисления числа π с использованием метода Монте-Карло
def calculate_pi(n, n_ring):
    for i in range(n):
        x = random.random() * 2
        y = random.random() * 2
        # Проверка, находится ли точка внутри окружности радиусом r с центром в (1,1)
        if pow(x - 1, 2) + pow(y - 1, 2) <= 1:
            n_ring += 1

    return 4 * r * r * n_ring / n


# Функция для вычисления дисперсии оценок числа π
def calculate_dispersion(pi_nums: list, avr_pi: float):
    squared_sum = 0
    for pi in pi_nums:
        squared_sum += pow(pi - avr_pi, 2)

    return squared_sum / len(pi_nums)


# Ввод радиуса окружности от пользователя
r = float(input("Введите радиус r окружности: "))

# Проведение экспериментов для разных значений n
for n in n_nums:
    print(f"\n\nДля n = {n}")
    avr_pi = 0
    pi_nums = []
    for i in range(10):
        print(f"Итерация i = {i + 1}")
        # Вычисление числа π и добавление его в список pi_nums
        pi = calculate_pi(n, 0)
        pi_nums.append(pi)
        print(f"Значение числа Пи на этой {i + 1} итерации: {pi}")
        avr_pi += pi/10 # Суммирование для последующего вычисления среднего значения

    print(f"Среднее значение числа Пи по итогам 10 итераций: {avr_pi}")
    # Вывод дисперсии оценок числа π
    print(f"Дисперсия: {calculate_dispersion(pi_nums, avr_pi)}")