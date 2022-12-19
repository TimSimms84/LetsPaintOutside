""" Define routes/endpoints for API """
from .schemas import EpisodeSchema
from .utils import find_value, color_dict, subject_dict, month_dict
from fastapi import Depends, HTTPException, APIRouter, Query, status
from initiate import Session, get_db
from typing import Optional


# Router provides blueprint for all endpoints
router = APIRouter(
    prefix="/api"
)


"get all episodes or all episodes by color name, subject name, or month."
@router.get("/")
def all_episodes(color_name: Optional[str] = Query(None),
                 subject_name: Optional[str] = Query(None),
                 month: Optional[str] = Query(None),
                 db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes endpoint """
    if color_name:
        column_name = find_value(color_dict, color_name)
        if not column_name:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Color not found")
        # Search for eps within column name based on color_name
        query = "SELECT * FROM episodes WHERE color_list LIKE '%{}%'".format(column_name)
        eps = db.execute(query).fetchall()
        if not eps:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No episodes found")
        return eps
    elif subject_name:
        column_name = find_value(subject_dict, subject_name)
        if not column_name:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Subject not found")
        # Search for eps within column name based on subject_name
        query = "SELECT * FROM episodes WHERE subject_list LIKE '%{}%'".format(column_name)
        eps = db.execute(query).fetchall()
        if not eps:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No episodes found")
        return eps
    elif month:
        column_name = find_value(month_dict, month)
        if not column_name:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Month not found")
        # Search for eps within column name based on month
        query = "SELECT * FROM episodes WHERE date LIKE '%{}%'".format(column_name)
        eps = db.execute(query).fetchall()
        if not eps:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No episodes found")
        return eps
    else:
        eps = db.execute("SELECT * FROM episodes").fetchall()
        if not eps:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No episodes found")
        return eps



@router.get("/{ep_id}")
def one_episode(ep_id: int, db: Session = Depends(get_db)):
    """ Define GET request made to endpoint with ep_id """
    query = "SELECT * FROM episodes WHERE id = {}".format(ep_id)
    ep = db.execute(query).fetchone()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    return ep


@router.post("/{ep_id}")
def add_episode(ep_id: int, ep: EpisodeSchema, db: Session = Depends(get_db)):
    """ Define POST request made to endpoint """
    query = "INSERT INTO episodes (id, title, date, color_list, subject_list) VALUES ({}, '{}', '{}', '{}', '{}')".format(
        ep_id, ep.title, ep.date, ep.color_list, ep.subject_list)
    db.execute(query)
    db.commit()
    return db.execute("SELECT * FROM episodes WHERE id = {}".format(ep_id)).fetchone()


@router.delete("/{ep_id}")
def delete_episode(ep_id: int, db: Session = Depends(get_db)):
    """ Define DELETE request made to endpoint including ep_id """
    query = "SELECT * FROM episodes WHERE id = {}".format(ep_id)
    ep = db.execute(query).fetchone()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    query = "DELETE FROM episodes WHERE id = {}".format(ep_id)
    db.execute(query)
    db.commit()
    return {"message": "Episode deleted"}


@router.get("/color/{color_id}")
def all_episodes_by_color(color_id: int,
                          db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/colors/:id endpoint """
    column_name = find_value(color_dict, color_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Color not found")
    # Search for eps within column name based on color_id
    query = "SELECT * FROM episodes WHERE color_list LIKE '%{}%'".format(column_name)
    eps = db.execute(query).fetchall()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps


@router.get("/subject/")
def all_episodes_by_subject_name(subject_name: str,
                                 db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/subject endpoint """
    column_name = find_value(subject_dict, subject_name)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Subject not found")
    # Search for eps within column name based on subject_id
    query = "SELECT * FROM episodes WHERE subject_list LIKE '%{}%'".format(column_name)
    eps = db.execute(query).fetchall()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps


@router.get("/subject/{subject_id}")
def all_episodes_by_subject(subject_id: int,
                            db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/subject/:id endpoint """
    column_name = find_value(subject_dict, subject_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Subject not found")
    # Search for eps within column name based on subject_id
    query = "SELECT * FROM episodes WHERE subject_list LIKE '%{}%'".format(column_name)
    eps = db.execute(query).fetchall()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps


@router.get("/month/{month_id}")
def all_episodes_by_month(month_id: int,
                          db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/month/:id endpoint """
    column_name = find_value(month_dict, month_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Month not found")
    # Search for eps where date column includes month based on month_id
    query = "SELECT * FROM episodes WHERE date LIKE '%{}%'".format(column_name)
    eps = db.execute(query).fetchall()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps
