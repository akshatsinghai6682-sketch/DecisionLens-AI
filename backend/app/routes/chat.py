"""Routes for chat and diagnostic conversation"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.agents.orchestrator import DecisionOrchestratorLangGraph
from app.models.session import Session as SessionModel
from app.models.decision import Decision
import uuid
import json

router = APIRouter(prefix="/chat", tags=["chat"])

# Initialize orchestrator
orchestrator = DecisionOrchestratorLangGraph()


@router.get("/questions")
async def get_diagnostic_questions():
    """Get diagnostic questions for decision"""
    questions = orchestrator.get_diagnostic_questions()
    return {
        "questions": questions,
        "total": len(questions)
    }


@router.post("/start-session")
async def start_chat_session(
    user_id: str,
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Start a new chat session"""
    
    # Verify decision exists
    decision = db.query(Decision).filter(Decision.id == decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    
    # Create session
    session = SessionModel(
        id=str(uuid.uuid4()),
        user_id=user_id,
        decision_id=decision_id,
        phase="diagnostic",
        messages=[]
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    
    return {
        "session_id": session.id,
        "phase": "diagnostic",
        "message": "Session started. Ready to begin diagnostic questions."
    }


@router.post("/send")
async def send_chat_message(
    session_id: str,
    message: str,
    db: Session = Depends(get_db)
):
    """Send message in chat session"""
    
    # Get session
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Add user message
    session.add_message("user", message)
    
    # Generate response based on phase
    if session.phase == "diagnostic":
        response = await _handle_diagnostic_response(session, orchestrator)
    else:
        response = {"message": "Session phase not recognized"}
    
    # Add assistant message
    session.add_message("assistant", response.get("message", ""))
    
    db.commit()
    db.refresh(session)
    
    return {
        "session_id": session_id,
        "response": response,
        "phase": session.phase
    }


@router.get("/session/{session_id}")
async def get_session_history(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Get chat session history"""
    
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {
        "session_id": session.id,
        "phase": session.phase,
        "messages": session.messages,
        "created_at": session.created_at
    }


async def _handle_diagnostic_response(session: SessionModel, orchestrator: DecisionOrchestratorLangGraph) -> dict:
    """Handle diagnostic phase response"""
    question_index = int(session.current_question_index)
    questions = orchestrator.get_diagnostic_questions()
    
    if question_index < len(questions):
        next_question = questions[question_index]
        session.current_question_index = str(question_index + 1)
        return {
            "message": next_question['question'],
            "category": next_question['category'],
            "examples": next_question['examples']
        }
    else:
        session.phase = "analysis"
        return {"message": "Diagnostic complete. Starting analysis..."}
