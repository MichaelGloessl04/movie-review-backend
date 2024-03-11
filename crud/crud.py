from types import NoneType
from sqlalchemy.orm import Session
from backend.crud.models import (Base, Movie, Genre,
                                 Director, Review, User)


class Crud:
    def __init__(self, engine):
        """
        Initializes the Crud class with the given database engine.
        """
        self._engine = engine
        Base.metadata.create_all(self._engine)

    def get_movies(self, id: int = None) -> list[Movie]:
        """
        Retrieves a list of movies from the database.

        Args:
            id (int, optional): The ID of the movie to retrieve. Defaults to
            None.

        Returns:
            list[Movie]: A list of Movie objects.
        """
        return self._get(Movie, id)

    def add_movie(self,
                  name: str,
                  poster_file: str,
                  release_date: str,
                  director_id: int) -> Movie:
        """
        Adds a new movie to the database.

        Args:
            name (str): The name of the movie.
            poster_file (str): The file path of the movie poster.
            release_date (str): The release date of the movie.
            genre_id (int): The ID of the genre associated with the movie.
            director_id (int): The ID of the director associated with the
            movie.

        Returns:
            Movie: The newly added Movie object.
        """
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name).__name__}")
        if not isinstance(poster_file, str):
            raise TypeError(f"Expected str, got {type(poster_file).__name__}")
        if not isinstance(release_date, int):
            raise TypeError(f"Expected int, got {type(release_date).__name__}")
        if not isinstance(director_id, int):
            raise TypeError(f"Expected int, got {type(director_id).__name__}")
        return self._add(Movie(
                        name=name,
                        poster_file=poster_file,
                        release_date=release_date,
                        director_id=director_id))

    def get_genres(self, id: int = None) -> list[Genre]:
        """
        Retrieves a list of genres from the database.

        Args:
            id (int, optional): The ID of the genre to retrieve.
            Defaults to None.

        Returns:
            list[Genre]: A list of Genre objects.
        """
        return self._get(Genre, id)

    def add_genre(self, name: str) -> Genre:
        """
        Adds a new genre to the database.

        Args:
            name (str): The name of the genre.

        Returns:
            Genre: The newly added Genre object.
        """
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name).__name__}")
        return self._add(Genre(name=name))

    def get_directors(self, id: int = None) -> list[Director]:
        """
        Retrieves a list of directors from the database.

        Args:
            id (int, optional): The ID of the director to retrieve.
            Defaults to None.

        Returns:
            list[Director]: A list of Director objects.
        """
        return self._get(Director, id)

    def add_director(self,
                     first_name: str,
                     last_name: str,
                     birth_date: int,
                     death_date: int,
                     country_of_origin: str) -> Director:
        """
        Adds a new director to the database.

        Args:
            first_name (str): The first name of the director.
            last_name (str): The last name of the director.
            birth_date (int): The birth date of the director.
            death_date (int): The death date of the director.
            country_of_origin (str): The country of origin of the director.

        Returns:
            Director: The newly added Director object.
        """
        if not isinstance(first_name, str):
            raise TypeError(f"Expected str, got {type(first_name).__name__}")
        if not isinstance(last_name, str):
            raise TypeError(f"Expected str, got {type(last_name).__name__}")
        if not isinstance(birth_date, int):
            raise TypeError(f"Expected int, got {type(birth_date).__name__}")
        if not isinstance(death_date, (int, NoneType)):
            raise TypeError(f"Expected int or NoneType, got {
                type(death_date).__name__}")
        if not isinstance(country_of_origin, str):
            raise TypeError(f"Expected str, got {
                type(country_of_origin).__name__}")
        return self._add(Director(
                        first_name=first_name,
                        last_name=last_name,
                        birth_date=birth_date,
                        death_date=death_date,
                        country_of_origin=country_of_origin))

    def get_reviews(self, id: int = None) -> list[Review]:
        """
        Retrieves a list of reviews from the database.

        Args:
            id (int, optional): The ID of the review to retrieve.
            Defaults to None.

        Returns:
            list[Review]: A list of Review objects.
        """
        return self._get(Review, id)

    def add_review(self,
                   rating: int,
                   review: str,
                   movie_id: int,
                   user_id: int) -> Review:
        """
        Adds a new review to the database.

        Args:
            rating (int): The rating of the review.
            review (str): The review text.
            movie_id (int): The ID of the movie associated with the review.
            user_id (int): The ID of the user associated with the review.

        Returns:
            Review: The newly added Review object.
        """
        if not isinstance(rating, int):
            raise TypeError(f"Expected int, got {type(rating).__name__}")
        if not isinstance(review, str):
            raise TypeError(f"Expected str, got {type(review).__name__}")
        if not isinstance(movie_id, int):
            raise TypeError(f"Expected int, got {type(movie_id).__name__}")
        if not isinstance(user_id, int):
            raise TypeError(f"Expected int, got {type(user_id).__name__}")
        return self._add(Review(
                        rating=rating,
                        review=review,
                        movie_id=movie_id,
                        user_id=user_id))

    def remove_review(self, id: int) -> None:
        """
        Removes a review from the database.

        Args:
            id (int): The ID of the review to remove.
        """
        self._remove(Review, id)

    def get_users(self, id: int = None) -> list[User]:
        """
        Retrieves a list of users from the database.

        Args:
            id (int, optional): The ID of the user to retrieve.
            Defaults to None.

        Returns:
            list[User]: A list of User objects.
        """
        return self._get(User, id)

    def add_user(self, username: str, email: str, password: str) -> User:
        """
        Adds a new user to the database.

        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The newly added User object.
        """
        if not isinstance(username, str):
            raise TypeError(f"Expected str, got {type(username).__name__}")
        if not isinstance(email, str):
            raise TypeError(f"Expected str, got {type(email).__name__}")
        if not isinstance(password, str):
            raise TypeError(f"Expected str, got {type(password).__name__}")
        return self._add(User(
                        username=username,
                        email=email,
                        password=password))

    def remove_user(self, id: int):
        """
        Removes a user from the database.

        Args:
            id (int): The ID of the user to remove.
        """
        self._remove(User, id)

    def _add(self, obj: Base):
        with Session(self._engine) as session:
            session.add(obj)
            session.commit()
            return session.query(obj.__class__) \
                .order_by(obj.__class__.id.desc()).first()

    def _get(self, obj: Base, id: int = None):
        with Session(self._engine) as session:
            if id:
                return session.query(obj).filter(obj.id == id).all()
            else:
                return session.query(obj).all()

    def _remove(self, obj: Base, id: int):
        with Session(self._engine) as session:
            session.query(obj).filter(obj.id == id).delete()
            session.commit()
