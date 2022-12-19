# Happy Lil Trees API

This will create a locally running API that will give you information from the 403 episodes of The Joy of Painting with Rob Ross.

# Criteria

You can make request to the API with the following criteria:

1) Broadcast Month
2) Subject Matter (What items are in the painting)
3) Color Palette

## Setup

To use the API you must have Python3 and SQLite installed. Then you simply clone the repo and run the `launch_api.sh` script to set everything up. The script will make sure `pip` and `venv` are installed for python, create a virtual environment using venv, and then install all the required files for the API in the virtual environment. This repo contains the three **original** data sources -- one of these sources needed to be transformed to used by pandas -- That file will be edited and saved in a new file. We then use pandas to read information from our files, do some basic editing to remove "unnecessary" information from our files, and then use SQLAlchemy to build our database in SQLite.

## Accessing the data

You can see the documentations at 
`http://127.0.0.1/docs/`

The API will run port 8000 and use `/api` as the first endpoint. `http://127.0.0.1:8000/api/` will list ALL episodes.

You can get a single episode by accessing. `http://127.0.0.1:8000/api/{ep_id}` 

To see episodes by subject matter you can access `http://127.0.0.1:8000/api/subject/{subject_id}`

To see episodes by month you can access
`http://127.0.0.1:8000/api/month/{month_id}`

To see episodes by color pallete you can access
`http://127.0.0.1:8000/api/color/{color_id}`

## Depencies
Python3 and SQLite are the only thing the user must have installed. The script will install the following

on the user machine:
pip (latest version)
venv (latest version)

in an venv instance:
FastAPI (0.73.0)
pandas (1.3.5)
pydantic (1.9.0)
request (2.27.1)
SQLAlchemy (1.4.31)


## Updating Database

You can add new episodes to the Database using a POST request to `http://127.0.0.1:8000/api/{ep_id}`  or delete entries by making a DELETE request to the same endpoint.

## Author
Tim Simms
