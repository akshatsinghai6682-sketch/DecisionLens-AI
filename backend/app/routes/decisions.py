"""Routes for decision endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.decision import DecisionCreate, DecisionResponse, DecisionListResponse, DecisionContextUpdate
from app.services.decision_service import DecisionService
from app.utils.db import get_db

router = APIRouter(prefix="/decisions", tags=["decisions"])


@router.post("/", response_model=DecisionResponse)
async def create_decision(
    user_id: str,
    decision: DecisionCreate,
    db: Session = Depends(get_db)
):
    """Create a new decision"""
    new_decision = DecisionService.create_decision(
        db,
        user_id,
        decision.title,
        decision.description
    )
    return new_decision


@router.get("/{decision_id}", response_model=DecisionResponse)
async def get_decision(
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Get decision by ID"""
    decision = DecisionService.get_decision(db, decision_id)
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision


@router.get("/user/{user_id}", response_model=DecisionListResponse)
async def list_user_decisions(
    user_id: str,
    db: Session = Depends(get_db)
):
    """List all decisions for a user"""
    decisions = DecisionService.list_user_decisions(db, user_id)
    return DecisionListResponse(decisions=decisions, total=len(decisions))


@router.patch("/{decision_id}/context")
async def update_decision_context(
    decision_id: str,
    context: DecisionContextUpdate,
    db: Session = Depends(get_db)
):
    """Update decision context"""
    updated_context = DecisionService.update_decision_context(
        db,
        decision_id,
        context.dict(exclude_unset=True)
    )
    return {"success": True, "context": updated_context}


@router.patch("/{decision_id}/complete")
async def mark_decision_complete(
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Mark decision as completed"""
    decision = DecisionService.mark_decision_complete(db, decision_id)
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return {"success": True, "decision": decision}
