import doctest


class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param make: Производитель транспортного средства
        :param model: Модель транспортного средства
        :param year: Год выпуска транспортного средства

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)
        """
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Год выпуска должен быть целым числом, больше или равным 1886")

        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """
        Запуск двигателя транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)
        >>> vehicle.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Остановка двигателя транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)
        >>> vehicle.stop_engine()
        """
        ...


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read_page(self) -> None:
        """
        Чтение одной страницы книги.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_page()
        """
        ...

    def bookmark_page(self, page_number: int) -> None:
        """
        Установка закладки на определенной странице.

        :param page_number: Номер страницы для закладки

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.bookmark_page(100)
        """
        if not isinstance(page_number, int) or page_number <= 0 or page_number > self.pages:
            raise ValueError("Номер страницы должен быть положительным целым числом и не превышать количество страниц")
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, storage: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param storage: Объем памяти (в ГБ)

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 13", 128)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Объем памяти должен быть положительным целым числом")

        self.brand = brand
        self.model = model
        self.storage = storage

    def install_app(self, app_size: int) -> None:
        """
        Установка приложения на смартфон.

        :param app_size: Размер приложения (в ГБ)

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 13", 128)
        >>> smartphone.install_app(2)

        """
        if not isinstance(app_size, int) or app_size <= 0:
            raise ValueError("Размер приложения должен быть положительным целым числом")
        ...

    def take_photo(self) -> None:
        """
        Сделать фотографию с помощью смартфона.

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 13", 128)
        >>> smartphone.take_photo()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации