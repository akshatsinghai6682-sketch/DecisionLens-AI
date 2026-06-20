"""Routes for authentication and user management"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserSelect
from app.utils.db import get_db
from app.models.user import User
import uuid

router = APIRouter(prefix="/auth", tags=["auth"])

# Mock users for MVP
MOCK_USERS = [
    {"id": "user-1", "email": "alex@example.com", "name": "Alex Chen"},
    {"id": "user-2", "email": "jordan@example.com", "name": "Jordan Smith"},
    {"id": "user-3", "email": "casey@example.com", "name": "Casey Morgan"},
]


@router.post("/signin", response_model=UserResponse)
async def mock_signin(user_select: UserSelect, db: Session = Depends(get_db)):
    """Mock sign-in endpoint (MVP - no real authentication)"""
    
    # Find user or create if doesn't exist
    user = db.query(User).filter(User.id == user_select.user_id).first()
    
    if not user:
        user = User(
            id=user_select.user_id,
            email=f"user-{user_select.user_id}@example.com",
            name=user_select.user_name,
            is_active=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    return user


@router.get("/users")
async def get_mock_users():
    """Get list of mock users for sign-in selection"""
    return {
        "users": MOCK_USERS,
        "message": "Mock users for MVP testing"
    }


@router.post("/signup", response_model=UserResponse)
async def mock_signup(user_create: UserCreate, db: Session = Depends(get_db)):
    """Mock sign-up endpoint (MVP - no real authentication)"""
    
    # Check if user exists
    existing = db.query(User).filter(User.email == user_create.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Create new user
    user = User(
        id=str(uuid.uuid4()),
        email=user_create.email,
        name=user_create.name,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


@router.post("/logout")
async def mock_logout():
    """Mock logout endpoint"""
    return {"message": "Logged out successfully"}
