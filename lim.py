import math


def lim(
        func: any,
        x: float,
        sharpness: float=1e-6
) -> tuple[float] | float:
    '''
    Функция находит предел функции в точке x с точностью до 0.000001

    :param func: исследуемая функция, должна принимать на вход только аргумент x и возвращать результат вычисления
    в формате float
    :param x: значение аргумента, в котором необходимо найти предел функции
    :param sharpness: точность поиска предела, по умолчанию 0.000001
    :return: предел, если он вычисляется в точке либо кортеж (левый предел, правый предел)
    '''
    # найдем правый предел
    try:
        coef = 0.1
        arg = x
        right_lim = func(arg + 1)
        temp_lim = func(arg + coef)

        while abs(temp_lim - right_lim) > sharpness:
            right_lim = temp_lim
            coef = coef / 10
            try:
                temp_lim = func(arg + coef)
            except ZeroDivisionError:
                right_lim = math.inf if right_lim > 0 else -math.inf
                break

    except Exception as e:
        print(e)
        right_lim = 0.0

    # найдем левый предел
    try:
        coef = 0.1
        arg = x
        left_lim = func(arg - 1)
        temp_lim = func(arg - coef)

        while abs(temp_lim - left_lim) > sharpness:
            left_lim = temp_lim
            coef = coef / 10
            try:
                temp_lim = func(x - coef)
            except ZeroDivisionError:
                left_lim = math.inf if left_lim > 0 else -math.inf
                break
    except Exception as e:
        print(e)
        left_lim = 0.0

    if math.isinf(left_lim) or math.isinf(right_lim):
        return left_lim, right_lim

    if abs(right_lim - left_lim) <= sharpness:
        return round((right_lim + left_lim) / 2, 6)
    else:
        return left_lim, right_lim


def test_func(x):
    return 4 * x + 3


def gapped_func(x):
    if x < 2.5:
        return 0.4 * x - 0.8
    else:
        return 4 - x


def hyperbola(x):
    return 8 / (x + 4) - 2


print(lim(test_func, 0))
print(lim(gapped_func, 2.5))
print(lim(hyperbola, -4))
