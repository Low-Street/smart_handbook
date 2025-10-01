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

        target_url = url or self.BASE_URL
        base_params = {
            "format": "json",
            "utf8": 1,
        }
        try:
            response = requests.get(
                target_url,
                params={**base_params, **(params or {})},
                headers=self.HEADERS,
                timeout=10,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException:
            raise
        try:
            return response.json()
        except ValueError as e:
            raise ValueError(f"Некорректный JSON-ответ от Wikipedia: {e}")
        
    def _lang_url(self, lang):
        """
        Создает URL API Wikipedia для указанного языка
        Args:
        lang: Код языка. например, ru для русской вики или en для английской

        Returns:
        URL API Wikipedia для выбранного языка
        """
        return f"https://{lang}.wikipedia.org/w/api.php"
    
    def _extract_from_pages(self, data):
        """
        Ддостаем первую страницу из структуры query.pages
        Возвращает словарь или None
        """
        pages = data.get("query", {}).get("pages", {})
        if not pages:
            return None
        for page in pages.values():
            return page
        return None

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
        url = self._lang_url(lang)
        params = {
            "action": "query",
            "prop": "extracts",
            "exintro": 1,
            "explaintext": 1,
            "redirects": 1,
            "titles": term,
        }
        data = self._make_request(params, url=url)

        page = self._extract_from_pages(data)
        if not page:
            return None
        if "missing" in page or not page.get("extract"):
            return None

        extract = page.get("extract", "")
        if not extract.strip():
            return None

        if chars > 0 and len(extract) > chars:
            trimmed = extract[:chars].rstrip()
            cut_pos = max(trimmed.rfind(". "), trimmed.rfind(" "), trimmed.rfind("—"))
            if cut_pos != -1 and cut_pos >= chars - 120:
                trimmed = trimmed[:cut_pos + 1]
            extract = trimmed + "…"
        return extract

    def get_full_article(self, term, lang="ru"):
        """
        Получает полный текст статьи из Wikipedia по заданному термину.

        Args:
            term: Термин для поиска.
            lang: Язык Wikipedia.

        Returns:
            Полный текст статьи или None.
        """
        url = self._lang_url(lang)
        params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "redirects": 1,
            "titles": term,
        }
        data = self._make_request(params, url=url)

        page = self._extract_from_pages(data)
        if not page or "missing" in page:
            return None

        extract = page.get("extract", "")
        if not extract.strip():
            return None
        return extract

    def get_article_url(self, term: str, lang="ru"):
        """
        Получает прямую ссылку на статью Wikipedia по заданному термину.

        Args:
            term: Термин для поиска.
            lang: Язык Wikipedia.

        Returns:
            URL статьи или None.
        """
        url = self._lang_url(lang)
        params = {
            "action": "query",
            "prop": "info",
            "inprop": "url",
            "redirects": 1,
            "titles": term,
        }
        data = self._make_request(params, url=url)

        page = self._extract_from_pages(data)
        if not page or "missing" in page:
            return None

        fullurl = page.get("fullurl") or page.get("canonicalurl")
        if fullurl:
            return fullurl
        return None

