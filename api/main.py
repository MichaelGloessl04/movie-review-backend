from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager

from backend.crud import create_engine, Crud
from . import api_types as ApiTypes

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


@app.get("/movies/")
def read_movies() -> List[ApiTypes.Movie]:
    return resource["crud"].get_movies()
