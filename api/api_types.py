from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str


class MovieNoID(BaseModel):
    title: str
    release_date: str
    genre: str
    director: str
    poster_file: str


class Movie(MovieNoID):
    id: int


class Genre(BaseModel):
    id: int
    name: str


class Review(BaseModel):
    id: int
    rating: int
    review: str
    movie_id: int
    user_id: int


class Director(BaseModel):
    id: int
    name: str
    birth_year: int
    death_year: int
    country: str
