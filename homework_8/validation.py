"""Validation"""


def validate(card_number):
    """Function printing python version."""
    card_number = str(card_number)
    length_even = len(card_number) % 2 == 0

    control_sum = 0
    i = 0

    for char in card_number:
        current_digit = int(char)

        if length_even and i % 2 != 0:
            number_check = current_digit
        elif not length_even and i % 2 == 0:
            number_check = current_digit
        else:
            number_check = current_digit * 2
            if number_check > 9:
                number_check -= 9

        control_sum += number_check
        i += 1

    return control_sum % 10 == 0


def main():
    """Function printing python version."""
    card_number = input("Введите номер карточки: ")
    print(validate(card_number))


main()
