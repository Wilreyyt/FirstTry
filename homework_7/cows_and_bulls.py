"""Cows and bulls"""
# pylint: disable-msg=C0103

import random

REPEAT = 1
RANDOM_NUMBER = ""

while REPEAT == 1:
    RANDOM_NUMBER = str(random.randint(1000, 9999 + 1))
    REPEAT = 0
    for character in RANDOM_NUMBER:
        if RANDOM_NUMBER.count(character) > 1:
            REPEAT = 1

INPUT_NUMBER = ""
while INPUT_NUMBER != RANDOM_NUMBER:
    REPEAT = 1
    while REPEAT == 1 or len(INPUT_NUMBER) != 4:
        INPUT_NUMBER = input("Введите ваше 4-значное число: ")
        REPEAT = 0
        for character in INPUT_NUMBER:
            if INPUT_NUMBER.count(character) > 1 or character < '0' or character > '9':
                REPEAT = 1

    BULLS_COUNT = 0
    for i in range(4):
        if INPUT_NUMBER[i] == RANDOM_NUMBER[i]:
            BULLS_COUNT += 1
    print("Быки:", BULLS_COUNT)

    COWS_COUNT = -BULLS_COUNT
    for j in INPUT_NUMBER:
        if j in RANDOM_NUMBER:
            COWS_COUNT += 1
    print("Коровы:", COWS_COUNT)
print("Вы выиграли!")
