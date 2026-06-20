"""Routes for scenario endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.scenario import ScenarioResponse, ScenariosComparisonResponse
from app.services.scenario_service import ScenarioService
from app.utils.db import get_db

router = APIRouter(prefix="/scenarios", tags=["scenarios"])


@router.get("/decision/{decision_id}")
async def get_decision_scenarios(
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Get all scenarios for a decision"""
    scenarios = ScenarioService.get_decision_scenarios(db, decision_id)
    return {
        "scenarios": scenarios,
        "total": len(scenarios)
    }


@router.get("/{scenario_id}", response_model=ScenarioResponse)
async def get_scenario(
    scenario_id: str,
    db: Session = Depends(get_db)
):
    """Get scenario with all perspectives"""
    scenario = ScenarioService.get_scenario_with_perspectives(db, scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenario


@router.post("/decision/{decision_id}/generate")
async def generate_scenarios(
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Trigger scenario generation for a decision"""
    # This would be called after diagnostic is complete
    # Implementation connects to orchestrator
    return {
        "message": "Scenario generation triggered",
        "decision_id": decision_id,
        "status": "processing"
    }
