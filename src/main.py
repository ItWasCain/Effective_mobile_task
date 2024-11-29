import sys

from outputs import export, pretty_output
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from base_config import Base, Book
import constants


def books_list(session):
    books = Book.get_all(session)
    results = [book.get_book_listed() for book in books]
    pretty_output(results)
    return constants.BOOKS_COUNT.format(Book.get_count(session))


def books_add(session):
    Book.book_add(
        session,
        title=input(constants.TITLE),
        author=input(constants.AUTHOR),
        year=input(constants.YEAR),
    )
    return constants.BOOK_ADDED


def books_update(session):
    book_id = int(input(constants.INPUT_ID))
    book = Book.get_book_by_id(book_id, session)
    if not book:
        return constants.WROND_ID
    pretty_output([book.get_book_listed()])

    status_id = input(constants.INPUT_STATUS)
    if status_id not in constants.STATUSES:
        return constants.WRONG_STATUS
    book.book_set_status(status_id, session)
    return constants.STATUS_ADDED


def books_delete(session):
    book_id = int(input(constants.INPUT_ID))
    book = Book.get_book_by_id(book_id, session)
    if not book:
        return constants.WROND_ID
    pretty_output(
        [book.get_book_listed()]
    )
    confirm = input(constants.DELETE_CONFIRMATION)
    if confirm == '1':
        Book.book_delete(book, session)
        return constants.BOOK_DELETED
    else:
        return constants.DELETION_CANCELLED


def books_search(session):
    search = input(constants.SEARCH)
    results = [
        book.get_book_listed() for book in Book.get_books_search(
            search, session
        )
    ]
    pretty_output(results)
    return constants.SEARCH_COMPLETED


def file_export(session):
    choice = input(constants.EXPORT_MENU)
    results = [book.get_book_listed() for book in Book.get_all(session)]
    export(results, choice)
    return constants.SAVED


MENU_CHOISE = {
    '1': books_list,
    '2': books_add,
    '3': books_update,
    '4': books_delete,
    '5': books_search,
    '6': file_export,
}


def main(session):
    choise = input(constants.MAIN_MENU)
    if choise not in MENU_CHOISE.keys():
        sys.exit()
    print(MENU_CHOISE[choise](session))
    main(session)


if __name__ == '__main__':
    engine = create_engine(constants.DATA_NAME, echo=False)
    Base.metadata.create_all(engine)
    session = Session(engine)
    main(session)
