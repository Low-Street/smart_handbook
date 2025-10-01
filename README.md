smart_handbook - эьо консольный справочник

Небольшое приложение для получения краткого определения термина из википедии (поддерживается русский и английский запрос)
Логика работы с API находится в модуле api_clients/wikipedia_client.py, пользовательский интерфейс в cli/main.py

-------------

Системные требования
- Python 3.10+
- Интернет-подключение
- Установленные зависимости (представлены в requirements.txt)

-------------

Как запустить?

Вводи в командую строку:
python3 -m venv .venv
.venv/bin/activate
pip3 install -r requirements.txt
python -m smart_handbook.cli.main "Интеграл" --lang ru