# Система управления библиотекой

Консольное приложение для управления библиотекой книг. Программа позволяет добавлять, удалять, искать и отображать книги, а также изменять их статус. Данные о книгах хранятся в файле JSON.

## Описание

Приложение выполняет следующие операции:
- **Добавление книги**: Пользователь может ввести название, автора и год издания книги, после чего она будет добавлена в библиотеку.
- **Удаление книги**: Пользователь может удалить книгу по её уникальному ID.
- **Поиск книги**: Книгу можно искать по названию, автору или году издания.
- **Отображение всех книг**: Программа может вывести список всех книг, хранящихся в библиотеке.
- **Изменение статуса книги**: Статус книги можно изменять на "в наличии" или "выдана".
- Код также покрыт тестами с помощью *unittest*

## Установка

1. Клонируйте репозиторий:
    ```bash
    https://github.com/Dontgoingforyou/library_management.git
   
2. Перейдите в каталог проекта:
    ```bash
   cd library_management
   
3. Установите зависимости:
    ```bash
   poetry install
   
4. Запустите программу
    ```bash
   python main.py

## Описание

1. После запуска программы, она предложит пользователю выбрать одну из доступных операций.
2. Для выполнения операции пользователю нужно будет ввести соответствующую команду в консоли.

## Пример работы программы
    1. Добавить книгу
    2. Удалить книгу
    3. Изменить статус книги
    4. Поиск книги
    5. Показать все книги
    6. Выйти
                
**Доступные команды**:
- Добавить книгу: Пользователь вводит название, автора и год издания.
- Удалить книгу: Необходимо ввести ID книги для её удаления.
- Изменить статус книги: Нужно ввести ID книги и новый статус ("в наличии" или "выдана").
- Поиск книги: Можно искать по названию, автору или году.
- Показать все книги: Выводит список всех книг.

## Тестирование

- Для тестирования проекта используется unittest. Чтобы запустить тесты, выполните следующую команду:
    ```bash
    python -m unittest tests.test_utils
  
**Тесты покрывают основные функции**:

- Добавление, удаление и изменение статуса книг.
- Поиск книг по различным критериям (название, автор, год).
- Обработка ошибок.

