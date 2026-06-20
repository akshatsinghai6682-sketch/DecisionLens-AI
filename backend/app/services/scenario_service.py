"""Scenario service - Business logic for scenarios"""

from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models.scenario import Scenario, AdvisorPerspective
import uuid


class ScenarioService:
    """Service for scenario operations"""

    @staticmethod
    def create_scenario(db: Session, decision_id: str, scenario_data: Dict[str, Any]) -> Scenario:
        """Create a new scenario"""
        scenario = Scenario(
            id=str(uuid.uuid4()),
            decision_id=decision_id,
            label=scenario_data.get('label', ''),
            narrative=scenario_data.get('narrative', ''),
            financial_score=scenario_data.get('financial_score', 0),
            career_score=scenario_data.get('career_score', 0),
            lifestyle_score=scenario_data.get('lifestyle_score', 0),
            risk_score=scenario_data.get('risk_score', 0),
            values_score=scenario_data.get('values_score', 0),
            confidence_level=scenario_data.get('confidence_level', 0.5),
            assumptions=scenario_data.get('assumptions', {})
        )
        db.add(scenario)
        db.commit()
        db.refresh(scenario)
        return scenario

    @staticmethod
    def add_advisor_perspective(db: Session, scenario_id: str, perspective_data: Dict[str, Any]) -> AdvisorPerspective:
        """Add advisor perspective to scenario"""
        perspective = AdvisorPerspective(
            id=str(uuid.uuid4()),
            scenario_id=scenario_id,
            advisor_type=perspective_data.get('advisor_type', ''),
            key_concern=perspective_data.get('key_concern', ''),
            recommendation=perspective_data.get('recommendation', ''),
            blind_spot_identified=perspective_data.get('blind_spot_identified', '')
        )
        db.add(perspective)
        db.commit()
        db.refresh(perspective)
        return perspective

    @staticmethod
    def get_decision_scenarios(db: Session, decision_id: str) -> List[Scenario]:
        """Get all scenarios for a decision"""
        return db.query(Scenario).filter(
            Scenario.decision_id == decision_id
        ).order_by(Scenario.created_at.asc()).all()

    @staticmethod
    def get_scenario_with_perspectives(db: Session, scenario_id: str) -> Scenario:
        """Get scenario with all advisor perspectives"""
        return db.query(Scenario).filter(
            Scenario.id == scenario_id
        ).first()
