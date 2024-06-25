from fastapi import APIRouter, Depends, HTTPException, Path, Query
from starlette import status
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from typing import Annotated
from models import Courses, UserCourses
from routers.auth import get_current_user
from fastapi.responses import FileResponse

import geopy.geocoders
import certifi
import ssl
from typing import Optional


ctx = ssl._create_unverified_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

router = APIRouter(prefix="/map", tags=["map"])

@router.get("/usermap")
async def root():
    return FileResponse("static/folium_map.html")


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# db_dependency = Annotated[Session, Depends(get_db)]
# user_dependency = Annotated[dict, Depends(get_current_user)]
#
# class UserCourseRequest(BaseModel):
#     garmin_id: int = Field(...)
#
#
# @router.get("/readall_ids", status_code=status.HTTP_200_OK)
# async def readall_ids(user: user_dependency, db: db_dependency):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return db.query(UserCourses).filter(UserCourses.user_id == user.get("id")).all()
#
#
# @router.get("/readall", status_code=status.HTTP_200_OK)
# async def readall(user: user_dependency, db: db_dependency):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#
#
#     # Query the database to fetch all course IDs associated with the user
#     course_ids = (
#         db.query(UserCourses.course_id)
#         .filter(UserCourses.user_id == user.get("id"))
#         .distinct()  # Select distinct course IDs
#         .all()
#     )
#
#     # Extract course IDs from the query result
#     course_ids = [course_id for course_id, in course_ids]
#
#     # Query the database to fetch all courses with the retrieved course IDs
#     courses = (
#         db.query(Courses)
#         .filter(Courses.id.in_(course_ids))  # Filter courses by the retrieved IDs
#         .all()
#     )
#
#     return courses
#
# @router.post("/add_course", status_code=status.HTTP_201_CREATED)
# async def create_todo(user: user_dependency, db: db_dependency, user_course_request: UserCourseRequest):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     todo_model = UserCourses(course_id=user_course_request.garmin_id, user_id=user.get("id"))
#     db.add(todo_model)
#     db.commit()
