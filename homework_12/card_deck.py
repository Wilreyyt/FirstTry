"""Card deck"""


from random import shuffle


class Card:
    """Карта"""
    number_list = [
        'T', '2', '3', '4', '5',
        '6', '7', '8', '9', '10',
        'J', 'Q', 'K'
    ]
    suit_list = [
        'Spades', 'Hearts',
        'Diamonds', 'Clubs'
    ]

    def __init__(self, number: str, suit: str):
        self.number = number
        self.suit = suit


class CardDeck:
    """Колода карт"""
    def __init__(self):
        self.cards = []
        for number in Card.number_list:
            for suit in Card.suit_list:
                card = Card(number, suit)
                self.cards.append(card)
        self.cards.append(Card("Joker", "Black"))
        self.cards.append(Card("Joker", "Red"))

    def shuffle(self):
        """Перемешать колоду"""
        shuffle(self.cards)

    def get(self, index: int) -> Card:
        """Получить карту по индексу"""
        return self.cards[index]


def main():
    """Основной код программы"""
    deck = CardDeck()
    deck.shuffle()

    card_number = int(input('Выберите карту из колоды в 56 карт: '))
    card = deck.get(card_number)

    print(f'Ваша карта: {card.number}, {card.suit}')


main()
