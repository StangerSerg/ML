def maniac_integrate(func, a, b, break_points=[], steps=10000):
    """
    Функция для особо опасных интегралов
    """
    print("🩸 Начинаем кровавое интегрирование...")

    # Собираем все подозрительные точки
    points = sorted(set([a] + break_points + [b]))
    total = 0

    for i in range(len(points) - 1):
        left, right = points[i], points[i + 1]
        print(f"✂️ Отрубаем кусок от {left} до {right}")

        # Проверяем, не улетает ли функция в бесконечность
        try:
            test_val = func((left + right) / 2)
            if abs(test_val) > 1e100:
                print(f"💀 Господин, мне не победить в этом бою, здесь сама Сингулярность")
                return float('inf') if test_val > 0 else float('-inf')
        except:
            print(f"💥 Сэйдза! Деление на ноль в середине!")
            return float('inf')

        # Интегрируем нормальный кусок
        try:
            piece = asigaru_integrate(func, left, right, steps)
            total += piece
            print(f" Добавили {piece:.4f}, всего набежало {total:.4f}")
        except ZeroDivisionError:
            print(f"💥 Сэйдза! Деление на ноль на участке {left} - {right}!")
            try:
                if left < right:
                    left += 1e-6
                    right -= 1e-6
                else:
                    left -= 1e-6
                    right += 1e-6
                piece = asigaru_integrate(func, left, right, steps)
                total += piece
                print(f" Добавили {piece:.4f}, всего набежало {total:.4f}")

            except ZeroDivisionError:
                print(f"Деление на ноль не удалось победить, господин! {left} - {right}!")
                return total

            except Exception as e:
                print(f"💀 Господин, я пал в бою с {e}")
                return total

        except Exception as e:
                print(f"💀 Господин, я пал в бою с {e}")
                return total

    print("Убираю меч в ножны, этот  бой окончен, жду следующего приказа, Даймё")
    return total


def asigaru_integrate(func, a, b, steps=10000):
    """Метод прямоугольников — тесак для ровных кусков"""
    h = (b - a) / steps
    return sum(func(a + i * h) for i in range(steps)) * h


def f(x):
    return 1 / x


print(f"Сегодня захвачено: {maniac_integrate(f, -10, 10, break_points=[0])}")
