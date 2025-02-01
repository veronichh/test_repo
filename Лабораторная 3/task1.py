class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Получение названия книги."""
        return self._name

    @property
    def author(self) -> str:
        """Получение автора книги."""
        return self._author

    def __str__(self) -> str:
        """Строковое представление книги."""
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self) -> str:
        """Репрезентация книги для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажных книг."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Вызов свойства для проверки

    @property
    def pages(self) -> int:
        """Получение количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Установка количества страниц с проверкой."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self) -> str:
        """Строковое представление бумажной книги."""
        return f"Бумажная книга '{self.name}'. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self) -> str:
        """Репрезентация бумажной книги для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

class AudioBook(Book):
    """Класс для аудиокниг."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Вызов свойства для проверки

    @property
    def duration(self) -> float:
        """Получение продолжительности аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Установка продолжительности с проверкой."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self) -> str:
        """Строковое представление аудиокниги."""
        return f"Аудиокнига '{self.name}'. Автор {self.author}. Продолжительность: {self.duration} часов"

    def __repr__(self) -> str:
        """Репрезентация аудиокниги для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Пример использования
if __name__ == "__main__":
    paper_book = PaperBook("1984", "George Orwell", 328)
    audio_book = AudioBook("Dune", "Frank Herbert", 21.5)

    print(paper_book)  # Вывод: Бумажная книга '1984'. Автор George Orwell. Страниц: 328
    print(repr(audio_book))  # Вывод: AudioBook(name='Dune', author='Frank Herbert', duration=21.5)