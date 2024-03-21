from math import tan, log, sin
import random


# функции, ограничивающие фигуру
# нижняя функция
def fun1(x):
    return log(x) + sin(x)


# верхняя функция
def fun2(x):
    return abs(tan(0.2 * x)) + x


# функция для расчёта площади фигуры методом Монте-Карло
def Monte_Carlo_method(L, M, N):
    return L * M / N


# функция для расчёта площади методом прямоугольников
def Rectangle_method(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = fun2(x) - fun1(x)
        ds = y * dx
        s += ds
        x += dx

    return s


# функция для расчёта площади методом трапеций
def Trapezoid_method(a, b, step):
    s = 0
    x = a

    while x <= b:
        y = fun2(x) + fun2(x + step) - (fun1(x) + fun1(x + step))
        mini_square = y / 2 * step
        s += mini_square
        x += step

    return s


# функция для нахождения минимального значения нижней функции и максимального значения верхней функции
def min_max(a, b, dx):
    x = a
    min_gx = fun1(x)
    max_fx = fun2(x)

    while x <= b:
        if min_gx > fun1(x):
            min_gx = fun1(x)
        if max_fx < fun2(x):
            max_fx = fun2(x)
        x += dx

    return [min_gx, max_fx]


# функция для проверки точки на попадание в фигуру
def xy_check(x, y):
    if fun1(x) <= y <= fun2(x):
        return True
    return False
