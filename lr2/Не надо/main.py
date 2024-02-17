def f(x):
    return (x + 2) / (x ** 2 - 2 * x - 3)

def qn(x, n):
    return (((-1) ** (n + 1)) - 5 / (3 ** (n + 1))) * x ** n

def Sum(x, e):
    n = 0
    summ = 0

    while True:
        fraction = qn(x, n)
        summ += fraction
        result = summ / 4
        if abs(f(x) - result) < e:
            return result
        n += 1

while True:
    x = float(input("Введите значение x: "))

    if abs(x) >= 1:
        print("\n\nРезультат:\n")
        print("Неверное значение х\n")
        print("-" * 40, "\n")
        continue

    e = float(input("Введите погрешность e: "))

    print("\n\nРезультат:\n")

    if e < 0:
        print("Неверное значение e\n")
        print("-" * 40, "\n")
        continue

    n = 0
    summ = 0

    # расчёт значения правой части равенства
    while True:
        fraction = ((-1) ** (n + 1) - 5 / (3 ** (n + 1))) * x ** n
        summ += fraction
        result = summ / 4
        if abs(f(x) - result) < e:
            break
        n += 1

    # вывод ответа
    print("Левая часть равенства      ", f"{f(x):<.6g}")
    print("Правая часть равенства     ", f"{result:<.6g}\n")
    print("-" * 40, "\n")