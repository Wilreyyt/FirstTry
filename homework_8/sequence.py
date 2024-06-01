"""Sequence"""
# pylint: disable-msg=C0103


def input_sequence():
    """Function printing python version."""
    sequence_length = int(input("Введите размер последовательности: "))
    sequence_elements = []
    for k in range(sequence_length):
        element = int(input(f"Введите элемент {k + 1}: "))
        sequence_elements.append(element)
    return sequence_elements


sequence = input_sequence()


def get_violating_index():
    """Function printing python version."""
    for i in range(len(sequence) - 1):
        # print(f"sequence[{i}] < sequence[{i + 1}]", \
        # sequence[i] < sequence[i + 1])
        if sequence[i] >= sequence[i + 1]:
            return i + 1
    return None


index = get_violating_index()

if index is None:
    print("Ваш список уже строго возрастающий")
else:
    del sequence[index]
    trues_count = 0
    for j in range(len(sequence) - 1):
        # print(f"sequence[{j}] < sequence[{j + 1}]", \
        # sequence[j] < sequence[j + 1])
        if sequence[j] < sequence[j + 1]:
            trues_count += 1
    if trues_count == len(sequence) - 1:
        print("True")
    else:
        print("False")
