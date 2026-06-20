"""Scenario and advisor perspective models"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Float, JSON, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class Scenario(Base):
    """Decision scenario simulation result"""

    __tablename__ = "scenarios"

    id = Column(String(36), primary_key=True, index=True)
    decision_id = Column(String(36), ForeignKey("decisions.id"), index=True)
    label = Column(String(255), index=True)  # Best case, Expected case, Worst case
    narrative = Column(Text)  # Detailed scenario description
    
    # Scoring (0-100)
    financial_score = Column(Float)
    career_score = Column(Float)
    lifestyle_score = Column(Float)
    risk_score = Column(Float)
    values_score = Column(Float)
    
    # Metadata
    confidence_level = Column(Float)  # 0-1
    assumptions = Column(JSON, default=dict)  # Key assumptions for this scenario
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    decision = relationship("Decision", back_populates="scenarios")
    advisor_perspectives = relationship("AdvisorPerspective", back_populates="scenario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Scenario {self.label}>"

    def get_weighted_score(self, weights: dict = None) -> float:
        """Calculate weighted score for scenario"""
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


class AdvisorPerspective(Base):
    """Advisor perspective for a scenario"""

    __tablename__ = "advisor_perspectives"

    id = Column(String(36), primary_key=True, index=True)
    scenario_id = Column(String(36), ForeignKey("scenarios.id"), index=True)
    advisor_type = Column(String(255), index=True)  # Parent, Entrepreneur, Academic, Counselor, Analyst
    key_concern = Column(Text)
    recommendation = Column(Text)
    blind_spot_identified = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    scenario = relationship("Scenario", back_populates="advisor_perspectives")

    def __repr__(self):
        return f"<AdvisorPerspective {self.advisor_type}>"
