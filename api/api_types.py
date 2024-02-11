from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str


class Movie(BaseModel):
    id: int
    title: str
    year: int
    genre: str
    description: str


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
