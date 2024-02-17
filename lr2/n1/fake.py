from math import tan, log, sin

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