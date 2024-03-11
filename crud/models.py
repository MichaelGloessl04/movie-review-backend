from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    poster_file: Mapped[str]
    release_date: Mapped[int]
    director_id: Mapped[int] = mapped_column(ForeignKey('director.id'))


class Genre(Base):
    __tablename__ = 'genre'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class MovieGenre(Base):
    __tablename__ = 'movie_genre'
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'),
                                          primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey('genre.id'),
                                          primary_key=True)


class Director(Base):
    __tablename__ = 'director'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_date: Mapped[int]
    death_date: Mapped[int] = mapped_column(nullable=True)
    country_of_origin: Mapped[str]


class Review(Base):
    __tablename__ = 'review'
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
    review: Mapped[str]
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    UniqueConstraint('username', 'email', name='unique_user')
