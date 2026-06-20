"""Scenario schemas for API"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any, List


class AdvisorPerspectiveResponse(BaseModel):
    """Advisor perspective response schema"""
    id: str
    advisor_type: str
    key_concern: str
    recommendation: str
    blind_spot_identified: str

    class Config:
        from_attributes = True


class ScenarioResponse(BaseModel):
    """Scenario response schema"""
    id: str
    label: str
    narrative: str
    financial_score: float
    career_score: float
    lifestyle_score: float
    risk_score: float
    values_score: float
    confidence_level: float
    assumptions: Dict[str, Any]
    advisor_perspectives: List[AdvisorPerspectiveResponse]
    created_at: datetime

    class Config:
        from_attributes = True

    def get_weighted_score(self, weights: Dict[str, float] = None) -> float:
        """Calculate weighted score"""
        if weights is None:
            weights = {
                'financial': 0.2,
                'career': 0.25,
                'lifestyle': 0.25,
                'risk': 0.15,
                'values': 0.15,
            }
        
        weighted = (
            self.financial_score * weights.get('financial', 0.2) +
            self.career_score * weights.get('career', 0.25) +
            self.lifestyle_score * weights.get('lifestyle', 0.25) +
            self.risk_score * weights.get('risk', 0.15) +
            self.values_score * weights.get('values', 0.15)
        )
        return round(weighted, 2)


class ScenariosComparisonResponse(BaseModel):
    """Scenarios comparison response"""
    scenarios: List[ScenarioResponse]
    recommended_weights: Dict[str, float]
    user_weights: Optional[Dict[str, float]] = None
