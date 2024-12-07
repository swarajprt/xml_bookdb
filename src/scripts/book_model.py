from pydantic import BaseModel
from fastapi import FastAPI

class Book(BaseModel):
    book_id: str
    author: str
    title: str
    price: str = None
    publish_date: str = None
    description : str = None