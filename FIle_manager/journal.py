'''
- **`__init__`**:
  - `filepath`: Путь к файлу, где хранятся записи журнала.
  - `entries`: Список для хранения объектов `Entry`.
  - Метод `load_entries()` вызывается сразу после инициализации объекта
  для загрузки существующих записей из файла.

**`add_entry`**:
  - Принимает объект `Entry` и добавляет его в список `entries`.
  - Вызывает `save_entries()` для обновления файла журнала.

**`save_entries`**:
  - Открывает файл журнала в режиме записи (`'w'`), что означает, что содержимое файла будет перезаписано.
  - Записывает каждую запись в файл, используя их строковое представление.

- **`load_entries`**:
  - Проверяет существование файла журнала. Если файла нет, метод возвращает `None`.
  - Читает весь файл и разделяет его на блоки по двойным переводам строк (`\n\n`), каждый из которых представляет одну запись.
  - Каждая запись разбивается на части по символу перевода строки (`\n`), и далее каждая строка разбивается по символу `:`, чтобы извлечь значения даты, автора и сообщения,
  которые затем используются для создания объектов `Entry`.
'''

import os

class Journal:
    '''
    - **`__init__`**:
  - `filepath`: Путь к файлу, где хранятся записи журнала.
  - `entries`: Список для хранения объектов `Entry`.
  - Метод `load_entries()` вызывается сразу после инициализации объекта
  для загрузки существующих записей из файла.
    '''
    def __init__(self, filepath):
        self.filepath = filepath
        self.entries = []
        self.load_entries()

    def add_entry(self, entry):
        self.entries.append(entry)
        self.save_entries()

    def save_entries(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            for entry in self.entries:
                f.write(str(entry) + "\n\n")


    '''
    **`load_entries`**:
  - Проверяет существование файла журнала. Если файла нет, метод возвращает `None`.
  - Читает весь файл и разделяет его на блоки по двойным переводам строк (`\n\n`), 
  каждый из которых представляет одну запись.
  - Каждая запись разбивается на части по символу перевода строки (`\n`), 
  и далее каждая строка разбивается по символу `:`, чтобы извлечь значения даты, 
  автора и сообщения,
  которые затем используются для создания объектов `Entry`.
  '''
    def load_entries(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        entries = content.split('\n\n')
        for entry in entries:
            if entry:
                parts = entry.split('\n')
                if len(parts) < 3:
                    continue
                date, author, message = parts
                date = date.split(': ')[1]
                author = author.split(': ')[1]
                message = message.split(': ')[1]
                self.entries.append(Entry(date, author, message))

    def update_entry(self, index, date=None, author=None, message=None):
        if 0 <= index < len(self.entries):
            if date:
                self.entries[index].date = date
            if author:
                self.entries[index].author = author
            if message:
                self.entries[index].message = message
            self.save_entries()

    def search_entries(self, keyword):
        return [entry for entry in self.entries if keyword.lower() in entry.message.lower()]

    def __str__(self):
        return "\n".join(str(entry) for entry in self.entries)

class Entry:
    def __init__(self, date, author, message):
        self.date = date
        self.author = author
        self.message = message

    def __str__(self):
        return f"Дата: {self.date}\nАвтор: {self.author}\nСообщение: {self.message}\n"