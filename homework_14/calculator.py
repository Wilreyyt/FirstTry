"""Калькулятор"""


from enum import Enum


OPERATORS_TO_PRIORITY = {
    "**": 1,
    "*": 2,
    "/": 2,
    "+": 3,
    "-": 3,
}


class LexemeTypes(Enum):
    """Типы лексем"""
    operator = "operator"
    number = "number"


class Lexeme:
    """Обозначает символ в выражении - число или оператор"""
    def __init__(self, value: str, lexeme_type: LexemeTypes):
        self.value = value
        self.type = lexeme_type


def parse_lexemes(lexemes: list[str]) -> list[Lexeme]:
    """Переводит строковые значения символов в лексемы"""
    result: list[Lexeme] = []
    for str_lexeme in lexemes:
        if str_lexeme in OPERATORS_TO_PRIORITY:
            lexeme = Lexeme(str_lexeme, LexemeTypes.operator)
        else:
            number = float(str_lexeme)
            lexeme = Lexeme(str(number), LexemeTypes.number)

        result.append(lexeme)

    return result


def validate_lexemes(lexemes: list[Lexeme]) -> bool:
    """Проверяет правильность ввода пользователя"""
    expected_type = LexemeTypes.number

    for lexeme in lexemes:
        if lexeme.type != expected_type:
            return False

        if expected_type == LexemeTypes.number:
            expected_type = LexemeTypes.operator
        elif expected_type == LexemeTypes.operator:
            expected_type = LexemeTypes.number
        else:
            return False

    return True


def calculate_operator(a: float, b: float, operator: str) -> float:
    """Вычислить значения, используя строку оператора"""
    if operator == '**':
        return a ** b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b

    raise ValueError("Некорректный оператор")


def resolve_operator(lexemes: list[Lexeme], priority: int) -> bool:
    """Выполнить вычисление одного оператора в списке лексем"""
    operator = None
    i = 0
    for lexeme in lexemes:
        if lexeme.type == LexemeTypes.operator \
        and OPERATORS_TO_PRIORITY[lexeme.value] == priority:
            operator = lexeme.value
            break
        i += 1

    if operator is not None:
        a = float(lexemes[i - 1].value)
        b = float(lexemes[i + 1].value)

        operator_result = calculate_operator(a, b, operator)

        lexemes[i] = Lexeme(str(operator_result), LexemeTypes.number)
        del lexemes[i + 1]
        del lexemes[i - 1]

        return True

    return False


def calculate_result(expression: str) -> float:
    """Калькулятор"""
    lexemes = parse_lexemes(expression.split())
    if not validate_lexemes(lexemes):
        raise ValueError("Выражение некорректно")

    first_priority = min(OPERATORS_TO_PRIORITY.values())
    last_priority = max(OPERATORS_TO_PRIORITY.values())

    for priority in range(first_priority, last_priority + 1):
        next_available = True
        while next_available:
            next_available = resolve_operator(lexemes, priority)

    return float(lexemes[0].value)


def main():
    """Основной код программы"""
    expression = input("Введите простое математическое выражение: ")

    try:
        result = calculate_result(expression)
    except ValueError:
        print("Произошла ошибка ввода!")
        return
    except Exception:
        print("Произошла ошибка")
        return
    print(result)


assert calculate_result("-6 + 5") == -1.0
assert calculate_result("6 ** 2 / 2 + 2") == 20.0
assert calculate_result("7 + 5 * 4 / 2") == 17.0

main()
