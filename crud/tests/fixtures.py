import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crud.crud import Crud
from crud.models import Movie, Genre, Director, User, Review

from .populate import populate


@pytest.fixture(scope="function")
def crud_in_memory():
    engine = create_engine("sqlite:///:memory:")
    session = sessionmaker(bind=engine)
    crud = Crud(engine, session)
    populate(session, Genre)
    populate(session, Movie)
    populate(session, Director)
    populate(session, User)
    populate(session, Review)
    yield crud, session
