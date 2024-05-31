"""Sequence"""
# pylint: disable-msg=C0103

sequence = [1, 3, 4, 7, 2, 9, 15, 21]
def solution():
    pass
def get_violating_index():
    for i in range(len(sequence) - 1):
        # print(f"sequence[{i}] < sequence[{i + 1}]", sequence[i] < sequence[i + 1])
        if sequence[i] >= sequence[i + 1]:
            return i + 1
    return None
index = get_violating_index()
if index == None:
    print("Ваш список уже строго возрастающий")
else:
    del sequence[index]
    trues_count = 0
    for j in range(len(sequence) - 1):
        # print(f"sequence[{j}] < sequence[{j + 1}]", sequence[j] < sequence[j + 1])
        if sequence[j] < sequence[j + 1]:
            trues_count += 1
    if trues_count == len(sequence) - 1:
        print("True")
    else:
        print("False")
