import random
from square_methods import fun1, fun2, Rectangle_method, Trapezoid_method, Monte_Carlo_method, min_max, xy_check

while True:
    # выбор метода
    print("Для выбора метода интегрирования введите требуемое число:")
    print("1 - метод прямоугольников")
    print("2 - метод трапеций\n")
    method = int(input())

    # ввод данных
    a = float(input("\nВведите нижний предел интегрирования a: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    step = float(input("Введите шаг интегрирования dx: "))

    if step <= 0 or b <= 0 or a <= 0:
        print("\nВведены неверные пределы интегрирования\n")
        continue

    N = int(input("\nВведите количество точек N: "))

    # вывод ответа
    print("\n\nРезультат:\n")

    if method == 1:
        print("Метод прямоугольников   ", f"{Rectangle_method(a, b, step):<.6g} ед. кв.")
    elif method == 2:
        print("Метод трапеций          ", f"{Trapezoid_method(a, b, step):<.6g} ед. кв.")
    else:
        print("Нет такого метода")

    from_y, to_y = min_max(a, b, step)

    M = 0

    # генерация точек для метода Монте-Карло
    for i in range(N + 1):
        x = random.uniform(a, b)
        y = random.uniform(from_y, to_y)

        if xy_check(x, y):
            M += 1

    L = abs(b - a) * abs(to_y - from_y)

    # вывод ответа
    print("Метод Монте-Карло       ", f"{Monte_Carlo_method(L, M, N):<.6g} ед. кв.\n")