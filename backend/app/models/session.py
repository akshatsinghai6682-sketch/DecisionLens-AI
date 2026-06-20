"""Session model for conversation tracking"""

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class Session(Base):
    """Chat session for decision conversation"""

    __tablename__ = "sessions"

    id = Column(String(36), primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), index=True)
    decision_id = Column(String(36), ForeignKey("decisions.id"), index=True)
    messages = Column(JSON, default=list)  # Conversation history
    phase = Column(String(255))  # diagnostic, tradeoff_review, simulation, perspective, etc.
    current_question_index = Column(String(10), default="0")
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="sessions")
    decision = relationship("Decision", back_populates="sessions")

    def __repr__(self):
        return f"<Session {self.id}>"

    def add_message(self, role: str, content: str, metadata: dict = None):
        """Add message to session"""
        if not self.messages:
            self.messages = []
        
        message = {
            "role": role,  # user, assistant
            "content": content,
            "timestamp": datetime.utcnow().isoformat(),
        }
        
        if metadata:
            message["metadata"] = metadata
        
        self.messages.append(message)
