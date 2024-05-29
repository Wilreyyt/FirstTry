"""Statues"""

import random
STATUES = []
for i in range(4):
    STATUE = 0
    while STATUE == 0 or STATUE in STATUES:
        STATUE = random.randint(1, 10)
    STATUES.append(STATUE)
print(STATUES)
MISSING_STATUES = 0
for i in range(min(STATUES), max(STATUES)):
    if i not in STATUES:
        MISSING_STATUES += 1
print("Кол-во пропущенных статуй: ", MISSING_STATUES)
