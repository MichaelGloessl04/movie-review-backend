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
        assert movie.release_date == "Oct 14, 1994"
        assert movie.director_id == 1
        assert movie.genres == session.query(Genre).filter(
            Genre.id.in_([1])).all()


def test_add_movie(crud_in_memory):
    crud_in_memory, session = crud_in_memory

    movie = crud_in_memory.add_movie(
        name="Pulp Fiction",
        poster_file="pulp_fiction.jpg",
        release_date="Oct 14, 1994",
        director_id=1,
        genres=["Crime", "Drama", "Thriller"]
    )

    with session() as session:
        assert isinstance(movie, Movie)
        assert movie.id == 4
        assert movie.name == "Pulp Fiction"
        assert movie.poster_file == "pulp_fiction.jpg"
        assert movie.release_date == "Oct 14, 1994"
        assert movie.director_id == 1
        assert movie.genres == session.query(Genre).filter(
            Genre.id.in_([1, 4, 5])).all()

    with session() as session:
        movie = session.query(Movie).get(movie.id)
        assert movie.name == "The Shawshank Redemption"
        assert movie.poster_file == "shawshank_redemption.jpg"
        assert movie.release_date == 19940923
        assert movie.director_id == 1
        assert movie.genres == session.query(Genre).filter(
            Genre.id.in_([1, 4, 5])).all()
