import random

# Задаем количество испытаний
N = 23

# Инициализируем списки для хранения результатов
S1, S2, SKG, SKH = [], [], [], []

# Цикл по испытаниям
for j in range(1, N + 1):
    n = 10000  # Число членов выборки
    w1 = 10    # Диапазон времен прихода от 0 до w1
    w2 = 5     # Диапазон времен обслуживания от 0 до w2

    g = []
    h = []

    L1 = []    # L1-распределение g
    L2 = []    # L2-распределение h

    Aa = 0     # Начальные значения
    Bb = w2 * random.random()
    Cc = 0
    Ee = Bb
    ff = Bb

    s1 = 0
    s2 = 0

    g.append(0)
    h.append(0)

    for k in range(11):
        L1.append(0)
        L2.append(0)

    for i in range(1, n):
        a = w1 * random.random()
        b = w2 * random.random()
        c = Cc + a
        if c > Ee:
            d = c
        else:
            d = Ee

        e = d + b
        f = e - c
        g.append(f - b)
        h.append(d - Ee)
        Cc = c
        Ee = e

        # Вычисление функций распределения – L1, L2 дискретных величин g, h
        if g[i] <= 1:
            L1[1] += 1

        if h[i] <= 0:
            L2[1] += 1

        for k in range(1, 11):
            if (g[i] > k - 1) and (g[i] <= k):
                L1[k] += 1
            if (h[i] > k - 1) and (h[i] <= k):
                L2[k] += 1

        if g[i] > 10:
            L1[10] += 1

        if h[i] > 10:
            L2[10] += 1

        s1 += g[i]
        s2 += h[i]

    # ниже - нормировка распределений величин g и h
    for i in range(0, 11):
        L1[i] = L1[i] / n
        L2[i] = L2[i] / n

    # Расчет средних значений величин g, h
    s1 = s1 / n
    s2 = s2 / n

    # ниже - расчет дисперсий величин g и h
    Dg = 0
    Dh = 0

    for i in range(n):
        Dg += pow(g[i] - s1, 2)
        Dh += pow(h[i] - s2, 2)

    Dg = Dg / n
    Dh = Dh / n

    # Расчет средне-квадратических отклонений величин g, h
    Skg = pow(Dg, 1/2)
    Skh = pow(Dh, 1/2)

    print(f"\nИспытание: {j}")

    print(f"g: {L1}")
    print(f"h: {L2}")

    print(f"Ср. зн. G: {s1}")
    S1.append(s1)
    print(f"Ср. зн. H: {s2}")
    S2.append(s2)

    print(f"Ср. кв отклон.Sg: {Skg}")
    SKG.append(Skg)
    print(f"Ср. кв отклон.Sh: {Skh}\n")
    SKH.append(Skh)

t = 2.58

epsilon_g = t * SKG[0] / pow(n, 1/2)
min_mg = S1[0] - epsilon_g
max_mg = S1[0] + epsilon_g

print(f"Ошибка ε для g: {epsilon_g} => {min_mg} < mg < {max_mg}")

epsilon_h = t * SKH[0] / pow(n, 1/2)
min_mh = S2[0] - epsilon_h
max_mh = S2[0] + epsilon_h

print(f"Ошибка ε для h: {epsilon_h} => {min_mh} < mh < {max_mh}")

failed_s = []
for s in S1:
    if not (min_mg < s < max_mg):
        failed_s.append(s)

print("Значения s1, не попадающие в доверительный интервал:")
print(failed_s)


for s in S2:
    if not (min_mh < s < max_mh):
        failed_s.append(s)

print("Значения s2, не попадающие в доверительный интервал:")
print(failed_s)
