"""Statues"""

import random
statues = []
for i in range(4):
    statue = 0
    while statue == 0 or statue in statues:
        statue = random.randint(1, 10)
    statues.append(statue)
statues.sort()
print(statues)
missing_statues = 0
for i in range(statues[0], statues[-1]):
    if i not in statues:
        missing_statues += 1
print("Кол-во пропущенных статуй: ", missing_statues)
