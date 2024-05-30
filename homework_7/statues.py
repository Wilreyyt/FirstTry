"""Statues"""
# pylint: disable-msg=C0103

import random
statues = []
for i in range(4):
    statue = 0
    while statue == 0 or statue in statues:
        statue = random.randint(1, 10)
    statues.append(statue)
print(statues)
missing_statues = 0
for i in range(min(statues), max(statues)):
    if i not in statues:
        missing_statues += 1
print("Кол-во пропущенных статуй: ", missing_statues)
