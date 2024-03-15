from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager

from sqlalchemy.orm import sessionmaker

from crud import create_engine, Crud

import api_types as ApiTypes

resource = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader
    """
    engine = create_engine("sqlite:///rdb.test.db")
    session = sessionmaker(bind=engine)
    resource["crud"] = Crud(engine, session)
    yield
    engine.dispose()
    resource.clear()
    print("lifespan ended")


app = FastAPI(lifespan=lifespan)


@app.get("/movies/")
def read_movies() -> List[ApiTypes.Movie]:
    crud = resource["crud"]
    movies = crud.get_movies()

    for movie in movies:
        movie.genres = crud.get_movie_genres(movie.id)

    return movies
