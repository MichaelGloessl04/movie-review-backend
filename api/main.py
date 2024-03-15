from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager

from crud import create_engine, Crud, Movie

import api_types as ApiTypes

resource = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader
    """
    engine = create_engine("sqlite:///rdb.test.db")
    resource["crud"] = Crud(engine)
    yield
    engine.dispose()
    resource.clear()
    print("lifespan ended")


app = FastAPI(lifespan=lifespan)


@app.get("/movie/")
def read_movies() -> List[ApiTypes.Movie]:
    return resource["crud"].get_movies()


@app.post("/movie/")
def add_movie(movie: ApiTypes.MovieNoID) -> ApiTypes.Movie:
    movie = resource["crud"].add_movie(
        Movie(
            title=movie.title,
            release_date=movie.year,
            genre_id=1,
            director_id=movie.director,
            poster_file=movie.poster_file,
        ))
    return movie
