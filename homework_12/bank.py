"""Bank"""


from calendar import monthrange


class Deposit:
    """Класс вклада"""
    def __init__(self, size: float, term_months: int):
        self.size = size
        self.term_months = term_months


class Currency:
    """Валюта"""
    def __init__(self, to_dollar: float, sign: str):
        self.to_dollar = to_dollar
        self.sign = sign


currencies = [
    Currency(0.31, 'BYN'),
    Currency(1, 'USD'),
    Currency(1.07, 'EUR'),
]


def get_currency(currency_name: str) -> Currency | None:
    """Получить валюту по обозначению"""
    for currency in currencies:
        if currency.sign == currency_name:
            return currency
        
    return None


class Person:
    """Держатель валюты"""
    def __init__(self, currency: str, amount: float) -> None:
        self.currency = currency
        self.amount = amount


class Bank:
    """Класс банк"""
    def __init__(self, percent: int):
        self.percent = percent

    def deposit(self, money: float, term_years: int):
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
    
    def exchange_currency(
            self,
            currency_from_name: str,
            count_from: float,
            currency_to_name: str = None
        ) -> float:
        """Вычислить курс валюты"""
        currency_from = get_currency(currency_from_name)

        if currency_to_name is None:
            currency_to = get_currency('BYN')
        else:
            currency_to = get_currency(currency_to_name)

        dollars = currency_from.to_dollar * count_from
        return round(dollars / currency_to.to_dollar, 2)


def main():
    """Основной код программы"""
    percent = 10
    bank = Bank(percent)

    vasya = Person('USD', 10)
    petya = Person('EUR', 5)

    result = bank.exchange_currency(vasya.currency, vasya.amount)
    print(f'{vasya.amount} {vasya.currency} = {result} BYN')

    result = bank.exchange_currency(petya.currency, petya.amount)
    print(f'{petya.amount} {petya.currency} = {result} BYN')

    result = bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
    print(f'{vasya.amount} {vasya.currency} = {result} EUR')

    result = bank.exchange_currency(petya.currency, petya.amount, 'USD')
    print(f'{petya.amount} {petya.currency} = {result} USD')


main()
