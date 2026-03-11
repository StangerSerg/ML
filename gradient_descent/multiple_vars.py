import numpy as np

x = np.array([1.5, 1.5])


def f(x):
    return (
            (x[0] - 1) ** 2 * (x[1] + 1) ** 4
            + (x[0] + 1) ** 4 * (x[1] - 1) ** 2
            + (x[0] - 3) ** 2 * (x[1] - 2) ** 2
    )


def dx(f, x, delta=1e-8):
    delta_x = x[0] + delta
    with_delta = np.array([delta_x, x[1]])
    res = (f(with_delta) - f(x)) / delta

    return res


def dy(f, x, delta=1e-8):
    delta_y = x[1] + delta
    with_delta = np.array([x[0], delta_y])
    res = (f(with_delta) - f(x)) / delta

    return res


def grad(x):
    return np.array([dx(f, x), dy(f, x)])


gamma = 0.0085
eps = 1e-17
max_iters = 10000
i = 0
f_old = f(x)
f_new = f_old + 1
grad_i = grad(x)

while (abs(f_new - f_old) > eps or (abs(grad_i[0]) > eps or abs(grad_i[1]) > eps)) and i < max_iters:
    f_old = f_new if i > 0 else f_old
    grad_i = grad(x)
    x = x - gamma * grad_i
    f_new = f(x)
    i += 1

# Вывод точки.
print('------------')
print('Финальное значение точки x:')
print(x)
print('Финальное значение f(x):')
print(f(x))
print("Градиент в точке:")
print(grad_i)
