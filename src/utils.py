import json


def load_books(path: str) -> list[dict]:
    """ Загрузка данных из файла JSON. """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(path: str, books: list[dict]) -> None:
    """ Сохранение данных в файл JSON. """

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(path: str, title: str, author: str, year: int) -> None:
    """ Добавление книги в библиотеку. """

    books = load_books(path)
    new_id = max((book['id'] for book in books), default=0) + 1
    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'status': 'В наличии'
    }
    books.append(new_book)
    save_books(path, books)
    print('\nКнига добавлена успешно')


def search_books(path: str, query: str) -> None:
    """ Поиск книги по названию, автору или году. """

    books = load_books(path)
    query = query.lower()
    results = [
        book for book in books
        if query in book['title'].lower()
        or query in book['author'].lower()
        or query in str(book['year'])
    ]

    if results:
        print('Найдены следующие книги:\n')
        for book in results:
            print(f"{book['id']}: {book['title']} - {book['author']} ({book['year']}) - {book['status']}")
    else:
        print("Книги по запросу не найдены.\n")


def display_books(path: str) -> None:
    """ Вывод списка всех книг. """

    books = load_books(path)
    if not books:
        print('Библиотека пуста\n')
        return

    print('Список всех книг:\n')
    for book in books:
        print(f"{book['id']}: {book['title']} - {book['author']} ({book['year']}) - {book['status']}")


def change_status(path: str, book_id: int, new_status: str) -> None:
    """ Изменение статуса книги на в 'в наличии' или 'выдана' """

    if new_status not in {'в наличии', 'выдана'}:
        print("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.\n")
        return

    books = load_books(path)
    for book in books:
        if book['id'] == book_id:
            book['status'] = new_status
            save_books(path, books)
            print(f"Статус книги с id {book_id} обновлен на '{new_status}'.")
            return


def delete_book(path: str, book_id: int) -> None:
    """ Удаление книги из библиотеки по id. """

    books = load_books(path)
    updated_books = [book for book in books if book['id'] != book_id]

    if len(books) == len(updated_books):
        print(f'Книга с ID {book_id} не найдена.')
        return

    save_books(path, updated_books)
    print(f"Книга с id {book_id} удалена.")