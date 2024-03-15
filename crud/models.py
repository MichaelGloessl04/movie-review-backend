from __future__ import annotations

from typing import List
from sqlalchemy import Column, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


movie_genre = Table(
    "movie_genre",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), primary_key=True),
    Column("genre_id", ForeignKey("genre.id"), primary_key=True),
)


class Movie(Base):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    poster_file: Mapped[str]
    release_date: Mapped[str]
    director_id: Mapped[int] = mapped_column(ForeignKey('director.id'))
    genres: Mapped[List[Genre]] = relationship(secondary=movie_genre,
                                               back_populates='movies')


class Genre(Base):
    __tablename__ = 'genre'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    movies: Mapped[List[Movie]] = relationship(secondary=movie_genre,
                                               back_populates='genres')


class Director(Base):
    __tablename__ = 'director'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_date: Mapped[str]
    death_date: Mapped[str] = mapped_column(nullable=True)
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
