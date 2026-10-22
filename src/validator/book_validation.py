from typing import Optional

from sqlmodel import  Field, SQLModel



class CreateBookRequest(SQLModel):
    title: str 
    author: str
    price: int
    condition: str
    is_sold: bool 
    user_id: int