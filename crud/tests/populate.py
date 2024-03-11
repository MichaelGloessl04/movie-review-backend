from crud.models import Movie, Genre, MovieGenre, Director, User, Review

MOVIES = [
        {
            "name": "The Shawshank Redemption",
            "poster_file": "shawshank_redemption.jpg",
            "release_date": 19940923,
            "director_id": 1,
        },
        {
            "name": "The Godfather",
            "poster_file": "godfather.jpg",
            "release_date": 19720324,
            "director_id": 2,
        },
        {
            "name": "The Dark Knight",
            "poster_file": "dark_knight.jpg",
            "release_date": 20080718,
            "director_id": 3,
        },
    ]

GENRES = [
        {"name": "Drama"},
        {"name": "Action"},
    ]

MOVIEGENRE = [
        {"movie_id": 1, "genre_id": 1},
        {"movie_id": 2, "genre_id": 1},
        {"movie_id": 3, "genre_id": 2},
]

DIRECTORS = [
        {
            "first_name": "Frank",
            "last_name": "Darabont",
            "birth_date": 19590128,
            "death_date": None,
            "country_of_origin": "USA",
        },
        {
            "first_name": "Francis Ford",
            "last_name": "Coppola",
            "birth_date": 19390407,
            "death_date": None,
            "country_of_origin": "USA",
        },
        {
            "first_name": "Christopher",
            "last_name": "Nolan",
            "birth_date": 19770730,
            "death_date": None,
            "country_of_origin": "UK",
        },
    ]

USER = [
        {
            "username": "user1",
            "email": "email1",
            "password": "password1",
        }
    ]

REVIEW = [
        {
            "rating": 5,
            "review": "Great movie",
            "movie_id": 1,
            "user_id": 1,
        }
    ]


def populate(session, obj):
    mock_values = []
    if obj == Movie:
        mock_values = MOVIES
    elif obj == Genre:
        mock_values = GENRES
    elif obj == MovieGenre:
        mock_values = MOVIEGENRE
    elif obj == Director:
        mock_values = DIRECTORS
    elif obj == User:
        mock_values = USER
    elif obj == Review:
        mock_values = REVIEW
    with session() as session:
        for movie in mock_values:
            session.add(obj(**movie))
            session.commit()
