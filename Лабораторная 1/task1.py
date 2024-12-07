# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

from abc import ABC, abstractmethod
import doctest


class Book(ABC):
    """Абстрактный класс для книги.

    Атрибуты:
    ----------
    title : str
        Название книги.
    author : str
        Автор книги.
    pages : int
        Количество страниц в книге.

    Методы:
    --------
    read() -> str
        Читает книгу.
    get_summary() -> str
        Возвращает краткое содержание книги.

    Примеры:
    --------
    >>> book = Book("1984", "George Orwell", 328)  # Это вызовет ошибку, так как Book абстрактный
    """

    def __init__(self, title: str, author: str, pages: int):
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self) -> str:
        """Читает книгу."""
        ...

    @abstractmethod
    def get_summary(self) -> str:
        """Возвращает краткое содержание книги."""
        ...


class Car(ABC):
    """Абстрактный класс для автомобиля.

    Атрибуты:
    ----------
    make : str
        Производитель автомобиля.
    model : str
        Модель автомобиля.
    year : int
        Год выпуска автомобиля.

    Методы:
    --------
    start() -> str
        Запускает двигатель автомобиля.
    stop() -> str
        Останавливает двигатель автомобиля.

    Примеры:
    --------
    >>> car = Car("Toyota", "Corolla", 2020)  # Это вызовет ошибку, так как Car абстрактный
    """

    def __init__(self, make: str, model: str, year: int):
        if not isinstance(make, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int) or year <= 1885:  # Первый автомобиль был создан в 1886
            raise ValueError("Год выпуска должен быть целым числом больше 1885")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self) -> str:
        """Запускает двигатель автомобиля."""
        ...

    @abstractmethod
    def stop(self) -> str:
        """Останавливает двигатель автомобиля."""
        ...

class Table(ABC):
    """Абстрактный класс для стола.

    Атрибуты:
    ----------
    material : str
        Материал стола.
    dimensions : tuple
        Размеры стола в формате (ширина, высота, глубина).

    Методы:
    --------
    assemble() -> str
        Собирает стол.
    disassemble() -> str
        Разбирает стол.

    Примеры:
    --------
    >>> table = Table("Wood", (120, 75, 60))  # Это вызовет ошибку, так как Table абстрактный
    """

    def __init__(self, material: str, dimensions: tuple):
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть строкой")
        if not isinstance(dimensions, tuple) or len(dimensions) != 3:
            raise ValueError("Размеры должны быть кортежем из трех элементов (ширина, высота, глубина)")

        self.material = material
        self.dimensions = dimensions

    @abstractmethod
    def assemble(self) -> str:
        """Собирает стол."""
        ...

    @abstractmethod
    def disassemble(self) -> str:
        """Разбирает стол."""
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации