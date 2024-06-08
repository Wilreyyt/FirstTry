"""Return number"""


def result_is_number(func):
    def wrapper(*args):
        result = func(*args)
        if not (isinstance(result, int) or isinstance(result, float)):
            print('Функция должна возвращать число')

        return result

    return wrapper


@result_is_number
def calculate_sum(a, b):
    return a + b


print(calculate_sum(4, 5))
print(calculate_sum('a', 'b'))
