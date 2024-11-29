import csv
import datetime as dt
import json

from prettytable import PrettyTable

import constants


def pretty_output(results):
    results = [constants.TABLE_HEAD, *results]
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def csv_export(results, RESULTS_DIR, now_formatted):
    results = [constants.FILE_HEAD, *results]
    file_path = RESULTS_DIR / constants.FILE_NAME_CSV.format(now_formatted)
    with open(file_path, 'w', encoding='utf-8') as f:
        csv.writer(
            f,
            dialect=csv.unix_dialect
        ).writerows(
            results
        )


def json_export(results, RESULTS_DIR, now_formatted):
    listed_books = []
    for book in results:
        book_dictionary = dict(zip(constants.FILE_HEAD, book))
        listed_books.append(book_dictionary)
    file_path = RESULTS_DIR / constants.FILE_NAME_JSON.format(now_formatted)
    with open(file_path, "w", encoding='utf-8') as final:
        json.dump(listed_books, final, ensure_ascii=False)


def export(results, choice):
    RESULTS_DIR = constants.BASE_DIR / constants.RESULTS
    RESULTS_DIR.mkdir(exist_ok=True)
    now_formatted = dt.datetime.now().strftime(constants.DATETIME_FORMAT)
    if choice == '1':
        csv_export(results, RESULTS_DIR, now_formatted)
    else:
        json_export(results, RESULTS_DIR, now_formatted)
