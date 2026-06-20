"""Scenario Simulation Agent - Generates scenario simulations"""

from typing import List, Dict, Any
from langchain.prompts import ChatPromptTemplate
import json


class ScenarioSimulatorAgent:
    """Agent responsible for simulating decision scenarios"""

    def __init__(self, llm):
        self.llm = llm

    async def generate_scenarios(self, decision_context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate best case, expected case, and worst case scenarios"""
        scenarios = []
        
        for scenario_type in ['best', 'expected', 'worst']:
            scenario = await self._generate_scenario(
                scenario_type,
                decision_context
            )
            scenarios.append(scenario)
        
        return scenarios

    async def _generate_scenario(self, scenario_type: str, decision_context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a specific scenario"""
        prompt = ChatPromptTemplate.from_template("""
        Generate a detailed {scenario_type} case scenario for this life decision.
        
        Decision: {title}
        Description: {description}
        User Values: {values}
        User Constraints: {constraints}
        Risk Tolerance: {risk_tolerance}
        Timeline: {timeline}
        
        For a {scenario_type} case, imagine:
        - {best_hint if scenario_type == 'best' else expected_hint if scenario_type == 'expected' else worst_hint}
        
        Provide detailed narrative and scoring:
        
        Return JSON with:
        {{
            "label": "{scenario_type_label}",
            "narrative": "Detailed 3-5 sentence description of this scenario",
            "financial_score": 0-100,
            "career_score": 0-100,
            "lifestyle_score": 0-100,
            "risk_score": 0-100 (higher = more risk/volatility),
            "values_score": 0-100 (alignment with user's values),
            "confidence_level": 0.0-1.0,
            "assumptions": {{"key": "assumption"}}
        }}
        
        Return ONLY valid JSON, no other text.
        """)

        scenario_hints = {
            'best': "Everything aligns perfectly. Best decisions made, opportunities appear, market conditions favorable.",
            'expected': "Realistic middle ground. Things go reasonably well. Some challenges, some wins. Most probable outcome.",
            'worst': "Significant challenges arise. Key assumptions fail. Market shifts unexpectedly. Major obstacles."
        }

        scenario_labels = {
            'best': 'Best Case',
            'expected': 'Expected Case',
            'worst': 'Worst Case'
        }

        messages = prompt.format_messages(
            scenario_type=scenario_type,
            best_hint=scenario_hints['best'] if scenario_type == 'best' else '',
            expected_hint=scenario_hints['expected'] if scenario_type == 'expected' else '',
            worst_hint=scenario_hints['worst'] if scenario_type == 'worst' else '',
            title=decision_context.get('title', ''),
            description=decision_context.get('description', ''),
            values=', '.join(decision_context.get('values', [])),
            constraints=str(decision_context.get('constraints', {})),
            risk_tolerance=decision_context.get('risk_tolerance', ''),
            timeline=decision_context.get('timeline', ''),
            scenario_type_label=scenario_labels[scenario_type]
        )

        response = await self.llm.ainvoke(messages)
        
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return self._default_scenario(scenario_type, scenario_labels[scenario_type])

    def _default_scenario(self, scenario_type: str, label: str) -> Dict[str, Any]:
        """Default scenario if LLM parsing fails"""
        if scenario_type == 'best':
            return {
                "label": label,
                "narrative": "All factors align positively. You make the right choice, opportunities emerge, and outcomes exceed expectations. You feel fulfilled and on the right path.",
                "financial_score": 85,
                "career_score": 90,
                "lifestyle_score": 85,
                "risk_score": 20,
                "values_score": 95,
                "confidence_level": 0.4,
                "assumptions": {"market_favorable": True, "personal_growth": True}
            }
        elif scenario_type == 'expected':
            return {
                "label": label,
                "narrative": "A realistic outcome where most factors work as expected. There are challenges and wins. You make progress toward your goals with some uncertainty and adjustment needed along the way.",
                "financial_score": 65,
                "career_score": 70,
                "lifestyle_score": 65,
                "risk_score": 50,
                "values_score": 75,
                "confidence_level": 0.75,
                "assumptions": {"moderate_success": True, "challenges_managed": True}
            }
        else:  # worst
            return {
                "label": label,
                "narrative": "Key assumptions fail. Market conditions worsen or personal circumstances change unexpectedly. You face significant challenges requiring adaptation and resilience.",
                "financial_score": 35,
                "career_score": 40,
                "lifestyle_score": 35,
                "risk_score": 85,
                "values_score": 45,
                "confidence_level": 0.5,
                "assumptions": {"major_challenges": True, "adjustment_required": True}
            }
