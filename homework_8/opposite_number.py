"""Opposite number"""


def find_opposite_number(first_number, n):
    """Function printing python version."""
    if first_number >= n or first_number < 0:
        return None
    if first_number > n / 2 - 1:
        return int(first_number - n / 2)
    return int(first_number + n / 2)


def main():
    """Function printing python version."""
    print("Введите количество чисел на окружности (обязательно четное!): ")
    n = int(input())
    if n % 2 != 0 or n <= 0:
        print("Ошибка! Введите число заново")
        return
    first_number = int(input("Введите любое целое число на окружности: "))
    opposite_number = find_opposite_number(first_number, n)
    if opposite_number is not None:
        print("Число напротив будет: ", opposite_number)
    else:
        print("Данное число не лежит на окружности")


main()
