"""Letters count"""


def append_count(string: str, char: str, count: int) -> str:
    """Добавить информацию о кол-ве символов в строку"""
    if count == 1:
        return string + char

    return string + f"{char}{count}"


def count_letters(string: str) -> str:
    """Подсчет символов в строке"""
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
    """Основной код программы"""
    assert count_letters("cccbba") == "c3b2a"
    assert count_letters("abeehhhhhccced") == "abe2h5c3ed"
    assert count_letters("aaabbceedd") == "a3b2ce2d2"
    assert count_letters("abcde") == "abcde"
    assert count_letters("aaabbdefffff") == "a3b2def5"


main()
