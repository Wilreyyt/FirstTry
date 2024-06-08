"""Type Decorator"""


def typed(arg_type):
    """Проверка типа параметра функции"""
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if isinstance(arg, arg_type):
                    new_args.append(arg)
                else:
                    new_args.append(arg_type(arg))

            return func(*new_args)

        return wrapper

    return decorator


@typed(str)
def add(a, b):
    """Строки"""
    return a + b


@typed(float)
def add_float(a, b):
    """Плавающая точка"""
    return a + b


@typed(int)
def add_int(a, b):
    """Числа"""
    return a + b


def main():
    """Основной код"""
    assert add(5, 6) == '56'
    assert isinstance(add_float(4, 2), float)
    assert isinstance(add_int(7, 11), int)


main()
