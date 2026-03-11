def f(x):
    return x ** 2


def f5(x):
    return (x + 5) ** 2


def y(x):
    return x ** 4 + 2 * x ** 2 - 10


def z(x):
    return x ** 6 - 5 * x ** 5 + x ** 4 - 1 / 2 * x ** 3 + 19

def downstairs(x):
    return -4 * x**4 + 5 * x**3 - 90 * x**2 - 2 * x + 1


def gradient_descent(f, x0, lr, max_step=100):
    x = x0
    for i in range(max_step):
        grad = df(f, x)
        diff_st = f"{grad=}"
        if abs(grad) < 1e-6:
            return x, i, diff_st
        x = x - lr * grad

    return x, max_step, diff_st


def df(f, x):
    dx = 1e-8
    res = (f(x + dx) - f(x)) / dx

    return res


print(f"{f5}, {gradient_descent(f5, 10, 0.01, 1000)}")
print(f"{z}, {gradient_descent(z, 10, 0.00005, 200000)}")
print(f"{z}, {gradient_descent(z, 0.1, 0.00005, 200000)}")
print(f"{z}, {gradient_descent(z, -5, 0.0002, 200000)}")
print(f"{y}, {gradient_descent(y, 10, 0.0001, 40000)}")




def explore_function(f, x_range=(-5, 6), steps=10000):
    """Просто посмотрим, как функция выглядит"""
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(x_range[0], x_range[1], steps)
    y = [f(xi) for xi in x]

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.title(f"Ландшафт функции {f.__name__}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

    # Найдём минимум простым перебором
    min_y = min(y)
    min_x = x[list(y).index(min_y)]
    print(f"Приблизительный минимум: x ≈ {min_x:.4f}, f(x) ≈ {min_y:.4f}")


explore_function(z)
