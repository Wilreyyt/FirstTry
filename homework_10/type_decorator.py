"""Type Decorator"""


def typed(type):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if isinstance(arg, type):
                    new_args.append(arg)
                else:
                    new_args.append(type(arg))

            return func(*new_args)

        return wrapper

    return decorator


@typed(str)
def add(a, b):
    return a + b


@typed(float)
def add_float(a, b):
    return a + b


@typed(int)
def add_int(a, b):
    return a + b


def main():
    assert add(5, 6) == '56'
    assert isinstance(add_float(4, 2), float)
    assert isinstance(add_int(7, 11), int)


main()
