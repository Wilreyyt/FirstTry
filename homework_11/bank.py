"""Bank"""


from calendar import monthrange


class Deposit:
    """Класс вклада"""
    def __init__(self, size: float, term_months: int):
        self.size = size
        self.term_months = term_months


class Bank:
    """Класс банк"""
    def __init__(self, percent: int):
        self.percent = percent

    def deposit(self, money: float, term_years: int) -> float:
        """Подсчет средств на счету после закрытия депозита"""
        deposit = Deposit(money, term_years * 12)
        percent_coefficient = self.percent / 100

        result_money = deposit.size

        for i in range(deposit.term_months):
            days_in_month = monthrange(2024, i % 12 + 1)[1]
            result_money += round(
                result_money * percent_coefficient / 366 * days_in_month,
                2
            )

        return round(result_money, 2)


def main():
    """Основной код программы"""
    percent = 10
    bank = Bank(percent)

    money = int(input('Введите количество денежных средств для вклада: '))
    term = int(input('Введите срок (лет): '))

    revenue = bank.deposit(money, term)
    print('Количество полученных средств:', revenue)


main()
