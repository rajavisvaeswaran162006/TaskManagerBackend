from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Literal
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str | None = None
    status: Literal["pending", "completed"] = "pending"
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: str | None = None
    status: Literal["pending", "completed"] | None = None
class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    status: str
    user_id: int
class Token(BaseModel):
    access_token: str
    token_type: str            