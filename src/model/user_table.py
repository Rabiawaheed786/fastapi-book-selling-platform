# src/model/user_table.py
from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field, Column, Enum as SqlAlchemyEnum
from typing import Optional, List




# user table model
class User(SQLModel, table=True):
     id: Optional[int] = Field(default=None, primary_key=True)
     username: str = Field(index=True, nullable=False)
     email: str = Field(unique=True, nullable=False)
     uni_name: str = Field(nullable=False)
     phone_number: str = Field(nullable=False)


     # one user can have many books
     books: List["Book"] = Relationship(back_populates="owner") #book table usr k table ko a ker mily
     
     created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
     updated_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

from .book_table import Book
User.model_rebuild()
