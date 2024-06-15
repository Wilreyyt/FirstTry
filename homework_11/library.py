"""Library"""


class Book:
    """Класс книга"""
    def __init__(
        self,
        name: str,
        author: str,
        page_count: int,
        isbn: int,
        is_reserved: bool
    ):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved


class User:
    """Класс пользователя"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.reserved_books = []
        self.taken_books = []

    def reserve_book(self, book: Book):
        """Резервирование книги"""
        if book.is_reserved:
            print('Книга уже зарезервирована другими пользователями')
            return

        self.reserved_books.append(book)
        book.is_reserved = True

    def take_book(self, book: Book):
        """Взятие книги"""
        if not book.is_reserved or book in self.reserved_books:
            self.taken_books.append(book)
            book.is_reserved = True
        else:
            print('Эта книга уже читается другими пользователями')

        if book in self.reserved_books:
            self.reserved_books.remove(book)

    def pass_book(self, book: Book):
        """Сдача книги"""
        if book in self.reserved_books:
            self.reserved_books.remove(book)
            book.is_reserved = False

        elif book in self.taken_books:
            self.taken_books.remove(book)
            book.is_reserved = False

        else:
            print('Вы не брали данную книгу')


def main():
    """Основной код программы"""
    books = [
        Book(
            'World of tanks',
            'Kuzovat Kuzovatovich',
            200,
            12345,
            False
        ),
        Book(
            'Chudo8585',
            'Kuzovat Kuzovatovich',
            180,
            12346,
            False
        ),
        Book(
            'Adventures of Gadjdukov',
            'Kuzovat Kuzovatovich',
            500,
            12347,
            False
        ),
        Book(
            'Kurnos',
            'Kuzovat Kuzovatovich',
            340,
            12348,
            False
        ),
        Book(
            'Karp',
            'Kuzovat Kuzovatovich',
            320,
            12349,
            False
        ),
    ]
    users = [
        User('Stepan', 'Bogdan'),
        User('Vladimir', 'Trekatol')
    ]
    users[0].reserve_book(books[1])
    users[1].take_book(books[3])

    me = User('Max', 'Lazar')

    print('Забронирована книга с индексом 2')
    me.reserve_book(books[2])

    print('Книга с индексом 4 взята на чтение')
    me.take_book(books[4])

    print('Книга с индексом 2 взята на чтение')
    me.take_book(books[2])

    print('Все книги прочитаны\n')
    me.pass_book(books[2])
    me.pass_book(books[4])

    print('Попытка взять книгу другого пользователя:')
    me.take_book(books[1])


main()
