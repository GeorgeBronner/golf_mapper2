from .utils import *
from routers.admin import get_db, get_current_user
from models import UserCourses
from starlette import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_assert():
    assert True