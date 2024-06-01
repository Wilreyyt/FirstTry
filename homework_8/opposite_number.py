"""Opposite number"""
# pylint: disable-msg=C0103

def main():
    print("Введите количество чисел на окружности (обязательно четное!): ")
    n = int(input())
    if n %2 != 0 or n <= 0:
        print("Ошибка! Введите число заново")
        return
    first_number = int(input("Введите любое целое число на окружности: "))
    if first_number >= n or first_number < 0:
        print("Данное число не лежит на окружности")
        return
    if first_number > n / 2 - 1:
        opposite_number = int(first_number - n / 2)
    else:
        opposite_number = int(first_number + n / 2)
    print("Число напротив будет: ", opposite_number)
main()
