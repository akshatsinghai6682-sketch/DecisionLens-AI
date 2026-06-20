"""User schemas for API"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    """User creation schema"""
    email: EmailStr
    name: str


class UserResponse(BaseModel):
    """User response schema"""
    id: str
    email: str
    name: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class UserSelect(BaseModel):
    """Mock user selection for MVP"""
    user_id: str
    user_name: str
