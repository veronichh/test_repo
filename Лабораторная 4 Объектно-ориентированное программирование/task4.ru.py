class Publication:
    """
    Базовый класс для всех видов публикаций.
    Определяет общие атрибуты и методы для описания публикации.
    """

    def __init__(self, title: str, author: str, publication_date: str, publisher: str) -> None:
#title: Название публикации. author: Автор публикации. publication_date: Дата публикации. publisher: Издатель публикации.
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.publisher = publisher
        self._views = 0  # Количество просмотров. Инкапсулирован, т.к. не должен изменяться напрямую извне.
        self._likes = 0  # Количество лайков. Инкапсулирован, т.к. не должен изменяться напрямую извне.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Publication.
        """
        return f"Publication: {self.title} by {self.author} ({self.publication_date})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Publication для отладки.
        """
        return f"Publication(title='{self.title}', author='{self.author}', publication_date='{self.publication_date}', publisher='{self.publisher}')"

    def get_views(self) -> int:
        """
        Возвращает количество просмотров публикации.
        """
        return self._views

    def like(self) -> None:
        """
        Увеличивает количество лайков на 1.
        """
        self._likes += 1

    def view(self) -> None:
        """
        Увеличивает количество просмотров на 1.
        """
        self._views += 1

    def get_citation(self) -> str:
        """
        Возвращает строку с цитатой публикации (автор, название, издатель, год).
        """
        return f"{self.author}. {self.title}. {self.publisher}, {self.publication_date[:4]}."



class NewsArticle(Publication):
    """
    Дочерний класс для новостных статей, унаследованный от Publication.
    """

    def __init__(self, title: str, author: str, publication_date: str, publisher: str, category: str, source: str) -> None:
        """
        Конструктор класса NewsArticle. Расширяет конструктор Publication, добавляя атрибуты category и source.

        Args:
            title: Название статьи.
            author: Автор статьи.
            publication_date: Дата публикации.
            publisher: Издатель статьи.
            category: Категория новости (политика, экономика, спорт и т.д.).
            source: Источник новости (название новостного сайта или агентства).
        """
        super().__init__(title, author, publication_date, publisher)
        self.category = category
        self.source = source
        self._urgency = "Normal"  # Степень срочности новости. Инкапсулирован, т.к. должен определяться внутри класса.

    def __str__(self) -> str:
        return f"NewsArticle: {self.title} by {self.author} ({self.publication_date}) - Category: {self.category}, Source: {self.source}"

    def __repr__(self) -> str:
        """
        Перегружает метод __repr__ для добавления информации о категории и источнике.
        Необходимо для более полной отладочной информации.
        """
        return f"NewsArticle(title='{self.title}', author='{self.author}', publication_date='{self.publication_date}', publisher='{self.publisher}', category='{self.category}', source='{self.source}')"


    def set_urgency(self, value: str) -> None:
        """
        Устанавливает степень срочности новости.
        """
        if value in ("High", "Normal", "Low"):
            self._urgency = value
        else:
            raise ValueError("Invalid urgency value. Use 'High', 'Normal', or 'Low'.")

    def get_urgency(self) -> str:
        return self._urgency

    def get_citation(self) -> str:
        """
        Перегружает метод get_citation для новостной статьи.
        Причина:  Цитата для новостной статьи должна включать название источника.
        """
        return f"{self.author}. {self.title}. {self.source}, {self.publication_date[:4]}."


    def share_on_social_media(self, platform: str) -> None:
        """
        Публикует новость в указанной социальной сети.
        """
        print(f"Sharing article '{self.title}' on {platform}...")
        # Должен быть код для отправки новости на соответствующую платформу


if __name__ == "__main__":
    publication = Publication("Bring Down The Stars", "Emma Scott", "2018-08-15", "Freedom")
    print(publication)
    print(repr(publication))
    publication.view()
    print(f"Views: {publication.get_views()}")

    article = NewsArticle("Economy is stronger despite uncertainty", "Cillian Keegan", "2019-04-18", "News Agency", "Economy", "Conservatives")
    print(article)
    print(repr(article))
    article.set_urgency("High")
    print(f"Urgency: {article.get_urgency()}")
    article.share_on_social_media("Twitter")
    print(f"Citation: {article.get_citation()}")