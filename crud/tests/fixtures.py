import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.crud.crud import Crud
from backend.crud.models import Movie, Genre, Director, User, Review
from backend.crud.tests.populate import populate


@pytest.fixture(scope="function")
def crud_in_memory():
    engine = create_engine("sqlite:///:memory:")
    crud = Crud(engine)
    session = sessionmaker(bind=engine)
    populate(session, Movie)
    populate(session, Genre)
    populate(session, Director)
    populate(session, User)
    populate(session, Review)
    yield crud
