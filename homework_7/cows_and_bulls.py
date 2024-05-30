"""Cows and bulls"""
# pylint: disable-msg=C0103

import random

repeat = 1
random_number = ""

while repeat == 1:
    random_number = str(random.randint(1000, 9999 + 1))
    repeat = 0
    for character in random_number:
        if random_number.count(character) > 1:
            repeat = 1

input_number = ""
while input_number != random_number:
    repeat = 1
    while repeat == 1 or len(input_number) != 4:
        input_number = input("Введите ваше 4-значное число: ")
        repeat = 0
        for character in input_number:
            if input_number.count(character) > 1 or character < '0' \
                                                 or character > '9':
                repeat = 1

    bulls_count = 0
    for i in range(4):
        if input_number[i] == random_number[i]:
            bulls_count += 1
    print("Быки:", bulls_count)

    cows_count = -bulls_count
    for j in input_number:
        if j in random_number:
            cows_count += 1
    print("Коровы:", cows_count)
print("Вы выиграли!")
