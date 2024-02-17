from math import tan, log, sin
import random

# нижняя функция
def fun1(x):
    return log(x) + sin(x)

# верхняя функция
def fun2(x):
    return abs(tan(0.2 * x)) + x

def Rectangle_method(a, b, step):
    full_square = 0
    x = a

    while x <= b:
        y = fun2(x) - fun1(x)
        mini_square = y * step
        full_square += mini_square
        x += step

    return full_square

def Trapezoid_method(a, b, step):
    s = 0
    x = a

    while x <= b:
        y = fun2(x) + fun2(x + step) - (fun1(x) + fun1(x + step))
        mini_square = y / 2 * step
        s += mini_square
        x += step

    return s

def Monte_Carlo_method(L, M, N):
    return L * M / N

def min_max(a, b, step):
    x = a
    min_gx = fun1(x)
    max_fx = fun2(x)

    while x <= b:
        if min_gx > fun1(x):
            min_gx = fun1(x)
        if max_fx < fun2(x):
            max_fx = fun2(x)
        x += step

    return [min_gx, max_fx]

# функция для проверки точки на попадание в фигуру
def xy_check(x, y):
    if fun1(x) <= y <= fun2(x):
        return True
    return False

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
        #print("Метод трапеций:", trapezoid_method(a, b, step))
        print("Метод трапеций          ", f"{Trapezoid_method(a, b, step):<.6g} ед. кв.\n")
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
    print('-' * 40, '\n')