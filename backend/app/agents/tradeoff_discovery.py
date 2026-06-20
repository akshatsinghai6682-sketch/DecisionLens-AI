"""Tradeoff Discovery Agent - Identifies hidden tradeoffs"""

from typing import List, Dict, Any
from langchain.prompts import ChatPromptTemplate
import json


class TradeoffDiscoveryAgent:
    """Agent responsible for discovering hidden tradeoffs"""

    def __init__(self, llm):
        self.llm = llm

    async def discover_tradeoffs(self, decision_context: Dict[str, Any]) -> List[Dict[str, str]]:
        """Discover hidden tradeoffs in decision"""
        prompt = ChatPromptTemplate.from_template("""
        Analyze this life decision and identify 5 hidden tradeoffs that the user might not immediately see.
        
        Decision Context:
        - Title: {title}
        - Description: {description}
        - Values: {values}
        - Constraints: {constraints}
        - Risk Tolerance: {risk_tolerance}
        - Timeline: {timeline}
        
        For each tradeoff, provide:
        1. Description: Clear explanation of the tradeoff
        2. Category: opportunity_cost|geographic|financial|time|growth|stability|social|health
        3. Impact: How it affects different life areas
        4. Hidden Nature: Why it's not immediately obvious
        
        Return ONLY valid JSON array with 5 objects, no other text.
        Example format:
        [
            {{
                "description": "By choosing startup, you trade stability for potential growth",
                "category": "stability_vs_growth",
                "impact": "High",
                "hidden_nature": "Users focus on salary difference but miss schedule control loss"
            }}
        ]
        """)

        messages = prompt.format_messages(
            title=decision_context.get('title', ''),
            description=decision_context.get('description', ''),
            values=', '.join(decision_context.get('values', [])),
            constraints=str(decision_context.get('constraints', {})),
            risk_tolerance=decision_context.get('risk_tolerance', ''),
            timeline=decision_context.get('timeline', '')
        )

        response = await self.llm.ainvoke(messages)
        
        try:
            tradeoffs = json.loads(response.content)
            return tradeoffs[:5]  # Limit to 5
        except json.JSONDecodeError:
            return self._default_tradeoffs()

    def _default_tradeoffs(self) -> List[Dict[str, str]]:
        """Default tradeoffs if LLM parsing fails"""
        return [
            {
                "description": "Short-term comfort vs. long-term growth",
                "category": "time",
                "impact": "High",
                "hidden_nature": "Easy to prioritize immediate needs over future development"
            },
            {
                "description": "Financial security vs. personal fulfillment",
                "category": "financial",
                "impact": "High",
                "hidden_nature": "Hard to quantify satisfaction; easy to overweight salary"
            },
            {
                "description": "Opportunity cost of chosen path",
                "category": "opportunity_cost",
                "impact": "Medium",
                "hidden_nature": "Invisible until path not taken closes"
            },
            {
                "description": "Geographic flexibility vs. community roots",
                "category": "geographic",
                "impact": "Medium",
                "hidden_nature": "Becomes important only after relocation"
            },
            {
                "description": "Skill specialization vs. career optionality",
                "category": "growth",
                "impact": "Medium",
                "hidden_nature": "Deep specialization reduces future pivots"
            }
        ]
