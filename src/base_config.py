from sqlalchemy import Column, Integer, String, or_
from sqlalchemy.orm import declarative_base, declared_attr

import constants


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Book(Base):
    title = Column(String(200))
    author = Column(String(200))
    year = Column(Integer)
    status = Column(String(20))

    def get_book_listed(self):
        return [
            self.id,
            self.title,
            self.author,
            self.year,
            self.status,
        ]

    @staticmethod
    def get_books_search(search, session):
        return session.query(Book).filter(
            or_(
                Book.title == search,
                Book.author == search,
                Book.year == search,
            )
        )

    @staticmethod
    def get_book_by_id(book_id, session):
        return session.query(Book).filter(Book.id == book_id).first()

    @staticmethod
    def get_all(session):
        return session.query(Book).all()

    @staticmethod
    def get_count(session):
        return session.query(Book).count()

    @staticmethod
    def book_delete(book, session):
        session.delete(book)
        session.commit()

    @staticmethod
    def book_add(session, title, author, year):
        session.add(
            Book(
                title=title,
                author=author,
                year=year,
                status=(constants.STATUS_IN_STOCK)
            )
        )
        session.commit()

    def book_set_status(self, status_id, session):
        if status_id == '1':
            self.status = constants.STATUS_IN_STOCK
        else:
            self.status = constants.STATUS_ISSUED
        session.commit()
