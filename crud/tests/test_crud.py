import pytest

from backend.crud.crud import Crud
from backend.crud.tests.populate import MOVIES, GENRES, DIRECTORS, USER, REVIEW

BADVALUES = {
    "str": "string",
    "int": 1,
    "float": 1.0,
    "NoneType": None,
    "list": ["list"],
    "dict": {"dict": "dict"},
    "tuple": ("tuple",)
}


def test_get_movies(crud_in_memory: Crud):
    _test_get(crud_in_memory.get_movies, MOVIES)


def test_add_movie(crud_in_memory: Crud):
    new_movie = {
        "name": "The Matrix",
        "poster_file": "the_matrix.jpg",
        "release_date": 19990331,
        "genre_id": 1,
        "director_id": 1
    }
    _test_add(crud_in_memory.add_movie, crud_in_memory.get_movies, new_movie)


def test_add_invalid_movie(crud_in_memory: Crud):
    movie = {
        "name": "str",
        "poster_file": "str",
        "release_date": "int",
        "genre_id": "int",
        "director_id": "int"
    }
    good_movie = {
        "name": "The Matrix",
        "poster_file": "the_matrix.jpg",
        "release_date": 19990331,
        "genre_id": 1,
        "director_id": 1
    }
    _test_add_invalid(movie, good_movie, crud_in_memory.add_movie)


def test_get_genres(crud_in_memory: Crud):
    _test_get(crud_in_memory.get_genres, GENRES)


def test_add_genre(crud_in_memory: Crud):
    new_genre = {"name": "Sci-Fi"}

    _test_add(crud_in_memory.add_genre, crud_in_memory.get_genres, new_genre)


def test_add_invalid_genre(crud_in_memory: Crud):
    genre = {"name": "str"}
    good_genre = {"name": "Sci-Fi"}
    _test_add_invalid(genre, good_genre, crud_in_memory.add_genre)


def test_get_directors(crud_in_memory: Crud):
    _test_get(crud_in_memory.get_directors, DIRECTORS)


def test_add_director(crud_in_memory: Crud):
    new_director = {
        "first_name": "Lana",
        "last_name": "Wachowski",
        "birth_date": 19650621,
        "death_date": None,
        "country_of_origin": "USA"
    }

    _test_add(crud_in_memory.add_director, crud_in_memory.get_directors,
              new_director)


def test_add_invalid_director(crud_in_memory: Crud):
    director = {
        "first_name": "str",
        "last_name": "str",
        "birth_date": "int",
        "death_date": ("int", "NoneType"),
        "country_of_origin": "str"
    }
    good_director = {
        "first_name": "Lana",
        "last_name": "Wachowski",
        "birth_date": 19650621,
        "death_date": None,
        "country_of_origin": "USA"
    }
    _test_add_invalid(director, good_director, crud_in_memory.add_director)


def test_get_reviews(crud_in_memory: Crud):
    _test_get(crud_in_memory.get_reviews, REVIEW)


def test_add_review(crud_in_memory: Crud):
    new_review = {
        "rating": 4,
        "review": "Good movie",
        "movie_id": 1,
        "user_id": 1
    }

    _test_add(crud_in_memory.add_review, crud_in_memory.get_reviews,
              new_review)


def test_add_invalid_review(crud_in_memory: Crud):
    review = {
        "rating": "int",
        "review": "str",
        "movie_id": "int",
        "user_id": "int"
    }
    good_review = {
        "rating": 4,
        "review": "Good movie",
        "movie_id": 1,
        "user_id": 1
    }
    _test_add_invalid(review, good_review, crud_in_memory.add_review)


def test_remove_review(crud_in_memory: Crud):
    _test_remove(crud_in_memory.remove_review, crud_in_memory.get_reviews,
                 REVIEW)


def test_get_users(crud_in_memory: Crud):
    _test_get(crud_in_memory.get_users, USER)


def test_add_user(crud_in_memory: Crud):
    new_user = {
        "username": "user2",
        "email": "email2",
        "password": "password2"
    }
    _test_add(crud_in_memory.add_user, crud_in_memory.get_users, new_user)


def test_add_invalid_user(crud_in_memory: Crud):
    user = {
        "username": "str",
        "email": "str",
        "password": "str"
    }
    good_user = {
        "username": "user2",
        "email": "email2",
        "password": "password2"
    }
    _test_add_invalid(user, good_user, crud_in_memory.add_user)


def test_remove_user(crud_in_memory: Crud):
    _test_remove(crud_in_memory.remove_user, crud_in_memory.get_users, USER)


def _test_get(func, reference):
    all_entities = func()
    assert len(all_entities) == len(reference)
    for movie, expected in zip(all_entities, reference):
        for key, value in expected.items():
            assert getattr(movie, key) == value

    for key, value in reference[0].items():
        assert getattr(func(1)[0], key) == value


def _test_add(add_func, get_func, new_entity):
    for key, value in new_entity.items():
        assert getattr(add_func(**new_entity), key) == value

    for key, value in new_entity.items():
        assert getattr(get_func()[-1], key) == value


def _test_add_invalid(map, good_entity, func):
    for key, values in map.items():
        if isinstance(values, tuple):  # TODO: Remove this if statement
            for bad_key, bad_value in BADVALUES.items():
                if bad_key not in values:
                    good_entity[key] = bad_value
                    with pytest.raises(TypeError):
                        func(**good_entity)
        else:
            for bad_key, bad_value in BADVALUES.items():
                if values != bad_key:
                    good_entity[key] = bad_value
                    with pytest.raises(TypeError):
                        func(**good_entity)


def _test_remove(remove_func, get_func, reference):
    assert len(get_func()) == len(reference)
    remove_func(1)
    assert len(get_func()) == len(reference) - 1
