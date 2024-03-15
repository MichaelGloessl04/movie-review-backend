import pytest

from crud.crud import Crud

from backend.crud.models import Movie, Genre, Director, User, Review


def test_get_movies(crud_in_memory):
    crud_in_memory, session = crud_in_memory
    movies = crud_in_memory.get_movies()
    assert len(movies) == 3

    for movie in movies:
        assert isinstance(movie, Movie)

    with session() as session:
        movie = session.query(Movie).get(movies[0].id)
        assert movie.name == "The Shawshank Redemption"
        assert movie.poster_file == "shawshank_redemption.jpg"
        assert movie.release_date == 19940923
        assert movie.director_id == 1
        assert movie.genres == session.query(Genre).filter(
            Genre.id.in_([1])).all()
