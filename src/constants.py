import os
from pathlib import Path

AUTHOR = 'Автор: '
BASE_DIR = Path(__file__).parent
BOOK_ADDED = 'Книга добавлена'
BOOK_DELETED = 'Книга удалена'
BOOKS_COUNT = 'Количество книг: {}\n'
DATA = os.path.join(BASE_DIR, 'data')
DATA_NAME = 'sqlite:///sqlite.db'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DELETE_CONFIRMATION = (
        'Вы уверены что хотите удалить книгу?\n'
        '1: Да\n'
        '2: Нет\n\n'
        '-->'
    )
DELETION_CANCELLED = 'Удаление отменено'
EXPORT_MENU = (
        'Выберете типа файла:\n'
        '1: csv\n'
        '2: json\n\n'
        '-->'
    )
FILE_HEAD = ['id', 'title', 'author', 'year', 'status']
FILE_NAME_CSV = 'library_{}.csv'
FILE_NAME_JSON = 'library_{}.json'
INPUT_ID = 'Введите id книги: '
INPUT_STATUS = (
        'Выберете новый статус:\n'
        '1: В наличии\n'
        '2: Выдана\n\n'
        '-->'
)
MAIN_MENU = (
        '\n1: Посмотреть библиотеку\n'
        '2: Создать запись\n'
        '3: Изменить статус\n'
        '4: Удалить книгу\n'
        '5: Поиск\n'
        '6: Экспорт в файл\n'
        '7: Выйти\n\n'
        '-->'
    )
RESULTS = 'results'
SEARCH = 'Поиск: '
SEARCH_COMPLETED = 'Поиск завершён'
STATUSES = ['1', '2']
STATUS_ADDED = 'Статус изменён'
STATUS_IN_STOCK = 'В наличии'
STATUS_ISSUED = 'Выдана'
SAVED = 'Файл сохранён'
TABLE_HEAD = ['id', 'Название', 'Автор', 'Год', 'Статус']
TITLE = 'Название: '
YEAR = 'Год: '
WROND_ID = 'Неверный id'
WRONG_STATUS = 'Неверный статус'
