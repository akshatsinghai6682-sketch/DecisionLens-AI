"""User model"""

from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class User(Base):
    """User account model (mock authentication for MVP)"""

    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    decisions = relationship("Decision", back_populates="user", cascade="all, delete-orphan")
    sessions = relationship("SessionModel", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.email}>"
