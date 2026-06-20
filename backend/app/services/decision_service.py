"""Decision service - Business logic for decisions"""

from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from app.models.decision import Decision, DecisionContext
from app.models.user import User
import uuid
from datetime import datetime


class DecisionService:
    """Service for decision operations"""

    @staticmethod
    def create_decision(db: Session, user_id: str, title: str, description: str) -> Decision:
        """Create a new decision record"""
        decision = Decision(
            id=str(uuid.uuid4()),
            user_id=user_id,
            title=title,
            description=description,
            status="in_progress"
        )
        db.add(decision)
        db.commit()
        db.refresh(decision)
        return decision

    @staticmethod
    def get_decision(db: Session, decision_id: str) -> Optional[Decision]:
        """Get decision by ID"""
        return db.query(Decision).filter(Decision.id == decision_id).first()

    @staticmethod
    def list_user_decisions(db: Session, user_id: str) -> List[Decision]:
        """List all decisions for a user"""
        return db.query(Decision).filter(
            Decision.user_id == user_id
        ).order_by(Decision.created_at.desc()).all()

    @staticmethod
    def update_decision_context(db: Session, decision_id: str, context_data: Dict[str, Any]) -> DecisionContext:
        """Update decision context"""
        context = db.query(DecisionContext).filter(
            DecisionContext.decision_id == decision_id
        ).first()

        if not context:
            context = DecisionContext(
                id=str(uuid.uuid4()),
                decision_id=decision_id
            )
            db.add(context)

        for key, value in context_data.items():
            if hasattr(context, key):
                setattr(context, key, value)

        db.commit()
        db.refresh(context)
        return context

    @staticmethod
    def mark_decision_complete(db: Session, decision_id: str) -> Decision:
        """Mark decision as completed"""
        decision = db.query(Decision).filter(Decision.id == decision_id).first()
        if decision:
            decision.status = "completed"
            decision.resolved_at = datetime.utcnow()
            db.commit()
            db.refresh(decision)
        return decision
