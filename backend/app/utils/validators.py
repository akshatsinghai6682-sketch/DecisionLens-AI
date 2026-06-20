"""Data validation utilities"""

import re
from typing import List, Dict, Any


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_decision_title(title: str) -> bool:
    """Validate decision title"""
    return len(title.strip()) >= 10 and len(title.strip()) <= 500


def validate_decision_description(description: str) -> bool:
    """Validate decision description"""
    return len(description.strip()) >= 20 and len(description.strip()) <= 5000


def validate_scenario_data(data: Dict[str, Any]) -> bool:
    """Validate scenario data structure"""
    required_fields = [
        'label',
        'narrative',
        'financial_score',
        'career_score',
        'lifestyle_score',
        'risk_score',
        'values_score',
    ]
    return all(field in data for field in required_fields)


def sanitize_text(text: str) -> str:
    """Sanitize text for safe storage"""
    return text.strip()[:5000]


def validate_score(score: float) -> bool:
    """Validate score is between 0-100"""
    return 0 <= score <= 100


def validate_weights(weights: Dict[str, float]) -> bool:
    """Validate scoring weights sum to 1.0"""
    total = sum(weights.values())
    return abs(total - 1.0) < 0.001
