"""Decision and decision context models"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
import json


class Decision(Base):
    """User decision record"""

    __tablename__ = "decisions"

    id = Column(String(36), primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), index=True)
    title = Column(String(500), index=True)
    description = Column(Text)
    status = Column(String(50), default="in_progress")  # in_progress, completed, archived
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="decisions")
    context = relationship("DecisionContext", back_populates="decision", uselist=False, cascade="all, delete-orphan")
    scenarios = relationship("Scenario", back_populates="decision", cascade="all, delete-orphan")
    tradeoffs = relationship("Tradeoff", back_populates="decision", cascade="all, delete-orphan")
    sessions = relationship("SessionModel", back_populates="decision", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Decision {self.title}>"


class DecisionContext(Base):
    """Decision context - user profile and constraints"""

    __tablename__ = "decision_contexts"

    id = Column(String(36), primary_key=True, index=True)
    decision_id = Column(String(36), ForeignKey("decisions.id"), unique=True, index=True)
    values_profile = Column(JSON, default=dict)  # Top 3-5 values
    constraints = Column(JSON, default=dict)  # Geographic, family, financial
    timeline = Column(String(255))  # Short-term, medium-term, long-term
    financial_situation = Column(String(255))  # Savings, debt, income
    risk_tolerance = Column(String(255))  # Low, medium, high
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    decision = relationship("Decision", back_populates="context")

    def __repr__(self):
        return f"<DecisionContext {self.decision_id}>"
