"""Statues"""

import random
STATUES = []
for i in range(4):
    STATUE = 0
    while STATUE == 0 or STATUE in STATUES:
        STATUE = random.randint(1, 10)
    STATUES.append(STATUE)
STATUES.sort()
print(STATUES)
MISSING_STATUES = 0
for i in range(STATUES[0], STATUES[-1]):
    if i not in STATUES:
        MISSING_STATUES += 1
print("Кол-во пропущенных статуй: ", MISSING_STATUES)
