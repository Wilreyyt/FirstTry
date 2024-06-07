"""Strings with #"""


def find_index(string_list: list[str], char: str) -> int | None:
    """Поиск индекса"""
    i = 0
    for current_char in string_list:
        if current_char == char:
            return i
        i += 1

    return None


def process_string(string: str) -> str:
    """Убрать решетки и предшествующие символы"""
    string_list = list(string)

    index = 0
    while index is not None:
        index = find_index(string_list, "#")
        if index is None:
            break

        del string_list[index]
        if index != 0:
            del string_list[index - 1]

    return "".join(string_list)


def main():
    """Основной код программы"""
    assert process_string("a#bc#d") == "bd"
    assert process_string("abc#d##c") == "ac"
    assert process_string("abc##d######") == ""
    assert process_string("#######") == ""
    assert process_string("") == ""

main()
