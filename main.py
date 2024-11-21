from config import FILE_PATH
from src.utils import add_book, delete_book, search_books, display_books, change_status


def main():
    """ Запуск программы """

    while True:
        print("\nМеню:\n")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти\n")

        user_choice = input('Выберите действие: ')
        if user_choice == '1':
            title = input('Введите название: ')
            author = input('Введите автора: ')
            year = int(input('Введите год издания: '))
            add_book(FILE_PATH, title, author, year)
        elif user_choice == '2':
            book_id = int(input('Введите id книги: '))
            delete_book(FILE_PATH, book_id)
        elif user_choice == '3':
            query = input('Введите строку для поиска:\n').lower()
            search_books(FILE_PATH, query)
        elif user_choice == '4':
            display_books(FILE_PATH)
        elif user_choice == '5':
            book_id = int(input('id книги: '))
            new_status = input('Новый статус (в наличии/выдана): ').lower()
            change_status(FILE_PATH, book_id, new_status)
        elif user_choice == '6':
            print('Завершение работы')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')

if __name__ == "__main__":
    main()