import requests


class WikipediaClient:
    """
    Клиент для взаимодействия с Wikipedia API.
    """

    BASE_URL = f"https://ru.wikipedia.org/w/api.php"

    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

    def _make_request(self, params, url: str | None = None):
        """
        Внутренний метод для выполнения запроса к Wikipedia API.
        """

        pass

    def get_summary(self, term, lang="ru", chars=500):
        """
        Получает краткое содержание статьи из Wikipedia по заданному термину.

        Args:
            term: Термин для поиска.
            lang: Язык Wikipedia (например, 'ru' для русской, 'en' для английской).
            chars: Максимальное количество символов в кратком содержании.

        Returns:
            Краткое содержание статьи или None, если статья не найдена или произошла ошибка.
        """
        pass

    def get_full_article(self, term, lang="ru"):
        """
        Получает полный текст статьи из Wikipedia по заданному термину.

        Args:
            term: Термин для поиска.
            lang: Язык Wikipedia.

        Returns:
            Полный текст статьи или None.
        """
        pass

    def get_article_url(self, term: str, lang="ru"):
        """
        Получает прямую ссылку на статью Wikipedia по заданному термину.

        Args:
            term: Термин для поиска.
            lang: Язык Wikipedia.

        Returns:
            URL статьи или None.
        """
        pass
