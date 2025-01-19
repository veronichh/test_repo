class Library:
    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список)
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Получение следующего идентификатора для добавления новой книги.

        :return: Идентификатор для новой книги
        """
        if not self.books:
            return 1
        else:
            return self.books[-1]["id"] + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Получение индекса книги по её идентификатору.

        :param book_id: Идентификатор книги
        :return: Индекс книги в списке
        :raise ValueError: Если книга с данным идентификатором не существует
        """
        for index, book in enumerate(self.books):
            if book["id"] == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования
if __name__ == "__main__":
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    # Класс Book для создания объектов книг (по желанию)
    class Book:
        def __init__(self, id_: int, name: str, pages: int):
            self.id = id_
            self.name = name
            self.pages = pages

    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    # Создаем список книг из BOOKS_DATABASE
    list_books = [
        {"id": book_dict["id"], "name": book_dict["name"], "pages": book_dict["pages"]}
        for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1
