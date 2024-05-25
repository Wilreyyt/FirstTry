"""Cows and bulls"""

import random
repeat = 1
random_number = ""

while repeat == 1:
    random_number = str(random.randint(1000, 9999 + 1))
    repeat = 0
    for i in random_number:
        if random_number.count(i) > 1:
            repeat = 1
input_number = ""
while input_number != random_number:
    input_number = input("Введите ваше 4-значное число: ")
    if len(input_number) == 4:
        bulls_count = 0
        for i in range(4):
            if input_number[i] == random_number[i]:
                bulls_count += 1
        print("Быки:", bulls_count)
        cows_count = - bulls_count
        for i in input_number:
            if i in random_number:
               cows_count += 1
        print("Коровы:",cows_count)
    else:
        print("Введите число заново!")
print("Вы выиграли!")
