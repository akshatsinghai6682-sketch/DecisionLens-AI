"""Decision schemas for API"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any


class DecisionCreate(BaseModel):
    """Decision creation schema"""
    title: str
    description: str


class DecisionContextUpdate(BaseModel):
    """Decision context update schema"""
    values_profile: Optional[List[str]] = None
    constraints: Optional[Dict[str, Any]] = None
    timeline: Optional[str] = None
    financial_situation: Optional[str] = None
    risk_tolerance: Optional[str] = None


class DecisionResponse(BaseModel):
    """Decision response schema"""
    id: str
    title: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    resolved_at: Optional[datetime]

    class Config:
        from_attributes = True


class DecisionListResponse(BaseModel):
    """List of decisions response"""
    decisions: List[DecisionResponse]
    total: int
