"""Candles"""


def count_candles(
        candle_count: int,
        remainder_count: int,
        remainders_for_new: int
) -> int:
    """Подсчет свечей"""
    if candle_count == 0:
        return 0

    remainders_derived = candle_count + remainder_count

    new_candle_count = remainders_derived // remainders_for_new
    remainders_left = remainders_derived % remainders_for_new

    count_from_remaining = count_candles(
        new_candle_count,
        remainders_left,
        remainders_for_new
    )

    return candle_count + count_from_remaining


def main():
    """Основной код программы"""
    initial_remainders = 0
    candle_count = int(input("Укажите текущее количество свечей: "))
    remainders_for_new = int(
        input("Сколько остатков нужно, чтобы собрать одну свечу?: ")
    )

    result = count_candles(candle_count, initial_remainders, remainders_for_new)

    print("Всего вы можете сжечь свечей:", result)


main()
