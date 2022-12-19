"""
Define schemas for posting/putting data to the database
Define Object structure for JSON data in request body
"""
from pydantic import BaseModel, Field
from typing import Optional, List


class EpisodeSchema(BaseModel):
    """ POST request fields -- all Optional """
    title: Optional[str] = Field(None, max_length=50)
    date: Optional[str] = Field(None, max_length=20)
    color_list: Optional[str] = Field(None, max_length=200)
    subject_list: Optional[str] = Field(None, max_length=200)

    class Config:
        orm_mode = True
