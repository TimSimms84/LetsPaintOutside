""" Initiate db for use in other modules """
from engine.db import SessionLocal
# Pretty sure this variable name is imported so "Session" can be used in views
from sqlalchemy.orm import Session
from typing import Generator


def get_db() -> Generator:
    """ Create and return db session and close properly when done """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
