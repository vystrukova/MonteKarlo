import random


# Функция для вычисления дисперсии оценок площади области
def calculate_dispersion(pi_nums: list, avr_pi: float):
    squared_sum = 0
    for pi in pi_nums:
        squared_sum += pow(pi - avr_pi, 2)

    return squared_sum / len(pi_nums)


# Заданные параметры для трех окружностей
n_nums = [100, 200, 500, 1000, 2000, 5000, 10000, 100000]

x = [0 for i in range(3)]
y = [0 for i in range(3)]
r = [0 for i in range(3)]
rr = [0 for i in range(3)]

# Ввод параметров окружностей
for j in range(3):
    print(f"{j + 1}-я окружность (x, y, r)")
    x[j] = int(input("x[j] = "))
    y[j] = int(input("y[j] = "))
    r[j] = int(input("r[j] = "))
    rr[j] = pow(r[j], 2)

xmin = x[0] - r[0]
ymin = y[0] - r[0]
d = r[0] * 2

# Проведение экспериментов для разных значений n
for n in n_nums:
    print(f"\n\nДля количества историй n = {n}")
    avr_S = 0
    S_nums = []

    for i in range(10):
        print(f"Итерация i = {i + 1}")
        m = 0
        for i in range(n):

            # Генерация случайных точек в прямоугольной области, ограниченной первой окружностью
            xp = random.random() * d + xmin
            yp = random.random() * d + ymin

            # Проверка, попадает ли точка внутрь всех трех окружностей
            is_hitted = 0

            for j in range(3):
                is_hitted += (pow(xp - x[j], 2) + pow(yp - y[j], 2) <= rr[j])

            if is_hitted == 3:
                m += 1

        # Оценка площади области с использованием отношения попаданий к общему числу точек
        S = pow(d, 2) * m/n
        S_nums.append(S)
        print(f"m = {m}")
        print(f"Значение площади на этой {i + 1} итерации: {S}")
        avr_S += S/10

    print(f"Среднее значение площади по итогам 10 итераций: {avr_S}")
    # Вывод дисперсии оценок площади
    print(f"Дисперсия: {calculate_dispersion(S_nums, avr_S)}")