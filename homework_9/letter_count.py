"""Letters count"""


def append_count(string: str, char: str, count: int) -> str:
    if count == 1:
        return string + char
    else:
        return string + f"{char}{count}"


def count_letters(string: str) -> str:
    if string == "":
        return ""

    result = ""

    current_char = string[0]
    current_char_count = 0
    for char in string:
        if char == current_char:
            current_char_count += 1
            continue

        result = append_count(result, current_char, current_char_count)

        current_char = char
        current_char_count = 1

    result = append_count(result, current_char, current_char_count)
    return result


def main():
    string = input("Введите строку: ")
    result = count_letters(string)

    print(result)


main()
