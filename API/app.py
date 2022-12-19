""" Driver program for application """
from api.episodes import models, views
from engine.db import engine, sessionmaker
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)
sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()

# Create new FastAPI instance
app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Bind routes to views as seen in api/v1/episodes/views.py
app.include_router(views.router)
