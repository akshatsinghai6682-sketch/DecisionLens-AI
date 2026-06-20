"""Advisor related schemas"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class AdvisorConfig(BaseModel):
    """Advisor configuration"""
    advisor_type: str
    persona: str
    key_characteristics: List[str]
    concern_focus: str


class PerspectivePanelRequest(BaseModel):
    """Request for perspective panel analysis"""
    decision_id: str
    scenario_context: Dict[str, Any]


class PerspectivePanelResponse(BaseModel):
    """Perspective panel response"""
    perspectives: List[Dict[str, Any]]
    consensus_areas: List[str]
    areas_of_disagreement: List[str]
