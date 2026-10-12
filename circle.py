import math


def area(r):
    """
    Вычисляет площадь круга по радиусу r.

    Пример вызова:
        area(2)
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по радиусу r.

    Пример вызова:
        perimeter(2)
    """
    return 2 * math.pi * r
