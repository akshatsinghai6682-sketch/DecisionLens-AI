"""Uncertainty Agent - Maps known and unknown factors"""

from typing import Dict, List, Any
from langchain.prompts import ChatPromptTemplate
import json


class UncertaintyAgent:
    """Agent for mapping uncertainty and assumptions"""

    def __init__(self, llm):
        self.llm = llm

    async def map_uncertainty(self, decision_context: Dict[str, Any], scenarios: list) -> Dict[str, Any]:
        """Map known vs unknown factors and assumptions"""
        prompt = ChatPromptTemplate.from_template("""
        Analyze the uncertainty landscape for this decision.
        
        Decision: {title}
        Description: {description}
        Scenarios: {scenarios_json}
        
        Identify:
        1. KNOWN FACTORS: What we know with reasonable certainty
        2. UNKNOWN FACTORS: Critical unknowns that could swing outcomes
        3. ASSUMPTIONS: What we're assuming to be true
        4. CONFIDENCE: How confident we are in our analysis
        
        Return JSON:
        {{
            "known_factors": [
                {{"factor": "description", "confidence": 0.9}}
            ],
            "unknown_factors": [
                {{"factor": "description", "impact": "high|medium|low"}}
            ],
            "key_assumptions": [
                "assumption1",
                "assumption2"
            ],
            "overall_confidence": 0.0-1.0,
            "what_would_change_outcome": ["event1", "event2"],
            "research_needed": ["research_area1", "research_area2"]
        }}
        
        Return ONLY valid JSON, no other text.
        """)

        messages = prompt.format_messages(
            title=decision_context.get('title', ''),
            description=decision_context.get('description', ''),
            scenarios_json=json.dumps(scenarios, indent=2)
        )

        response = await self.llm.ainvoke(messages)
        
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return self._default_uncertainty_map()

    def _default_uncertainty_map(self) -> Dict[str, Any]:
        """Default uncertainty map if LLM parsing fails"""
        return {
            "known_factors": [
                {"factor": "Your personal values and constraints", "confidence": 0.85},
                {"factor": "Current market salary data", "confidence": 0.7},
                {"factor": "Immediate time commitment", "confidence": 0.9}
            ],
            "unknown_factors": [
                {"factor": "Future career trajectory", "impact": "high"},
                {"factor": "Market conditions in 5 years", "impact": "high"},
                {"factor": "Personal preferences evolution", "impact": "medium"},
                {"factor": "Unexpected life changes", "impact": "high"}
            ],
            "key_assumptions": [
                "You remain interested in this field",
                "Market demand continues for this career",
                "Personal circumstances remain relatively stable",
                "Learning ability stays consistent"
            ],
            "overall_confidence": 0.65,
            "what_would_change_outcome": [
                "Major market shift in your field",
                "Significant personal life change",
                "New unexpected opportunity",
                "Technology disruption of your career path"
            ],
            "research_needed": [
                "Industry trends and forecasts",
                "Career satisfaction data",
                "ROI on educational paths",
                "Market salary projections"
            ]
        }
