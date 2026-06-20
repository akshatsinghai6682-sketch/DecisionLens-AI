"""Tradeoff model"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class Tradeoff(Base):
    """Hidden tradeoff identified in decision"""

    __tablename__ = "tradeoffs"

    id = Column(String(36), primary_key=True, index=True)
    decision_id = Column(String(36), ForeignKey("decisions.id"), index=True)
    description = Column(Text)
    category = Column(String(255))  # Opportunity cost, Geographic, Financial, etc.
    surfaced_by = Column(String(255))  # Which agent surfaced this
    acknowledged = Column(Boolean, default=False)  # User acknowledged this tradeoff
    user_notes = Column(Text, nullable=True)  # User's notes on this tradeoff
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    decision = relationship("Decision", back_populates="tradeoffs")

    def __repr__(self):
        return f"<Tradeoff {self.category}>"
