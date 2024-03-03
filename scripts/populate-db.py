import os
import requests
from backend.crud import create_engine, Crud

API_BASE_URL = "https://api.themoviedb.org/3"

if os.path.exists('movies.db'):
    os.remove('movies.db')

crud = Crud(create_engine('sqlite:///movies.db'))

image_url = "https://image.tmdb.org/t/p/w500"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5Yjg5NDFjZjAxNjBlZWU5ODUxZDU4ZTczYmY3Y2IyYiIsInN1YiI6IjY1NzFjYmUzYTIyZDNlMDBmZWVmMjM0ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Kva96cfeuCH9Q4RwTGJUSSpP5XDj34gZjDX5lMyx-Tg"  # noqa: E501
}

running = True
page = 0
movies_fetched = 0
desired_movies = 10


while running:
    page += 1

    title = ''
    release_date = 0
    genres = []

    director_id = 0
    director_name = ''
    director_surname = ''
    director_birth_date = 0
    director_death_date = 0
    director_country = ''

    movies_url = f"{API_BASE_URL}/movie/popular?language=en-US&page={page}"
    try:
        with requests.get(movies_url, headers=headers) as movies:
            movies.raise_for_status()
            for movie in movies.json()["results"]:
                if movies_fetched >= desired_movies:
                    running = False
                    break
                title = movie["title"]
                release_date = movie["release_date"]
                poster = movie["poster_path"]

                genre_url = f"{API_BASE_URL}/movie/{movie['id']}"
                with requests.get(genre_url, headers=headers) as genre_info:
                    genre_info.raise_for_status()
                    genre_info = genre_info.json()
                    for genre in genre_info["genres"]:
                        # add genre to db and get its id
                        genres.append(crud.add_genre(genre["name"]).id)

                credits_url = f"{API_BASE_URL}/movie/{
                    movie['id']}/credits?language=en-US"
                with requests.get(credits_url, headers=headers) as credits:
                    credits.raise_for_status()
                    for person in credits.json()["crew"]:
                        if person["job"] == "Director":
                            person_url = f"{API_BASE_URL}/person/{
                                person['id']}?language=en-US"
                            with requests.get(
                                person_url, headers=headers
                            ) as person_info:
                                person_info.raise_for_status()
                                person_info = person_info.json()
                                director_id = crud.add_director(
                                    person_info["name"].split(' ')[0],
                                    person_info["name"].split(' ')[1],
                                    person_info["birthday"],
                                    person_info["deathday"],
                                    person_info["place_of_birth"]).id
                crud.add_movie(title,
                               poster,
                               release_date,
                               genres[0],
                               director_id)
                movies_fetched += 1
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        continue

print(crud)
