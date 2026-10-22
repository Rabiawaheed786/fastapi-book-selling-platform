# src\routes\order_route.py
from fastapi import APIRouter
from src.model.user_table import User
from src.service.auth import verify_api_key
from src.utils.api_response import UserResponse
from fastapi.params import Depends
from sqlmodel import Session
from src.db.engine import get_session
from src.validator.user_validation import CreateUserRequest


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


# localhost:8000/user
@router.post("/", response_model= UserResponse)
async def create_user(userdata: CreateUserRequest, session:Session = Depends(get_session),api_key: str = Depends(verify_api_key)):
      """create a new user in the database"""
# database sy entery kerwai
      user = User(
          username=userdata.username,
          email=userdata.email,
          uni_name=userdata.uni_name,
          phone_number=userdata.phone_number
      )
  # database ma insert kerwai
      # add user to database
      session.add(user)
      session.commit()
      session.refresh(user)

      return UserResponse(status= "success", message="User created successfully", user=user)






