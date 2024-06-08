"""Positive Function Arguments"""


def validate_arguments(func):
    def wraper(*args):
        for arg in args:
            if arg <= 0:
               raise ValueError("Все аргументы должны быть положительными")
        return func(*args)

    return wraper


@validate_arguments
def print_numbers(a: int, b: int, c: int):
    print(a, b, c)


print_numbers(1, 2, 5)
print_numbers(1, -2, 5)
