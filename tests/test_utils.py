import json
import os
import unittest

from config import TEST_FILE_PATH
from src.utils import load_books, save_books, add_book, display_books, change_status, delete_book, search_books


class TestLibraryUtils(unittest.TestCase):

    def setUp(self):
        """ Создание временного файла для тестов. """

        self.temp_file = TEST_FILE_PATH
        self.file_path = self.temp_file.name

    def tearDown(self):
        """ Удаление временного файла после тестов. """

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_load_books_empty(self):
        """ Тест загрузки пустого файла. """

        books = load_books(self.file_path)
        self.assertEqual(books, [])

    def test_save_books(self):
        """ Тест сохранения данных в файл. """

        books = [{
            "id": 1,
            "title": "книга 1",
            "author": "автор 1",
            "year": 2024,
            "status": "в наличии"
        }]
        save_books(self.file_path, books)

        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.assertEqual(data, books)

    def test_add_book(self):
        """ Тест добавления книги. """

        add_book(self.file_path, 'книга 2', 'автор 2', 2023)
        books = load_books(self.file_path)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'книга 2')

    def test_change_status(self):
        """ Тест изменения статуса книги. """

        add_book(self.file_path, 'книга 3', 'автор 3', 2022)
        change_status(self.file_path, 1, 'выдана')
        books = load_books(self.file_path)
        self.assertEqual(books[0]['status'], 'выдана')

    def test_delete_book(self):
        """ Тест удаления книги. """

        add_book(self.file_path, 'книга 4', 'автор 4', 2021)
        delete_book(self.file_path, 1)
        books = load_books(self.file_path)
        self.assertEqual(len(books), 0)

    def test_display_books(self):
        """ Тест отображения всех книг. """

        add_book(self.file_path, 'книга 5', 'автор 5', 2020)
        try:
            display_books(self.file_path)
        except Exception as e:
            self.fail(f'display_books вызвал исключение {e}')

    def test_search_books(self):
        """ Тест поиска книг. """

        add_book(self.file_path, 'книга 6', 'автор 6', 2019)
        add_book(self.file_path, 'книга 7', 'автор 7', 2019)
        add_book(self.file_path, 'книга 8', 'автор 8', 2019)
        search_books(self.file_path, query='книга 6')
        search_books(self.file_path, query='2019')

        with open(self.file_path, 'r', encoding='utf-8') as file:
            json.load(file)


if __name__ == "__main__":
    unittest.main()
