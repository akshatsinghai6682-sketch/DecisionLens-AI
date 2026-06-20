"""Perspective Panel Agent - Generates diverse advisor perspectives"""

from typing import Dict, List, Any
from langchain.prompts import ChatPromptTemplate
import json


class PerspectivePanelAgent:
    """Agent for generating diverse advisor perspectives"""

    def __init__(self, llm):
        self.llm = llm
        self.advisors = [
            {
                "type": "Pragmatic Parent",
                "persona": "Practical, family-focused, values stability and proven paths",
                "focus": "Risk mitigation and financial security"
            },
            {
                "type": "Risk-Taking Entrepreneur",
                "persona": "Bold, opportunity-focused, comfortable with uncertainty",
                "focus": "Upside potential and learning opportunities"
            },
            {
                "type": "Cautious Academic",
                "persona": "Analytical, evidence-based, prefers research and data",
                "focus": "Long-term impact and skill development"
            },
            {
                "type": "Values-First Counselor",
                "persona": "Empathetic, values-aligned, holistic wellbeing",
                "focus": "Life satisfaction and authentic self"
            },
            {
                "type": "Data-Driven Analyst",
                "persona": "Metrics-focused, probability-based, removes emotion",
                "focus": "Quantifiable outcomes and trend analysis"
            }
        ]

    async def generate_perspectives(self, decision_context: Dict[str, Any], scenarios: list) -> List[Dict[str, Any]]:
        """Generate perspectives from 5 advisor archetypes"""
        perspectives = []
        
        for advisor in self.advisors:
            perspective = await self._generate_perspective(advisor, decision_context, scenarios)
            perspectives.append(perspective)
        
        return perspectives

    async def _generate_perspective(self, advisor: Dict[str, str], decision_context: Dict[str, Any], scenarios: list) -> Dict[str, Any]:
        """Generate perspective from specific advisor"""
        prompt = ChatPromptTemplate.from_template("""
        You are a {advisor_type}. {persona}
        
        Analyze this decision from your unique perspective:
        
        Decision: {title}
        Description: {description}
        User's Values: {values}
        User's Constraints: {constraints}
        
        Scenarios being considered:
        {scenarios_json}
        
        Provide your perspective as {advisor_type}:
        
        Return JSON:
        {{
            "advisor_type": "{advisor_type}",
            "key_concern": "Your main concern about this decision",
            "recommendation": "Your recommended path and why",
            "blind_spot_identified": "What you think the user might be missing",
            "questions_to_consider": ["question1", "question2", "question3"]
        }}
        
        Return ONLY valid JSON, no other text.
        """)

        messages = prompt.format_messages(
            advisor_type=advisor['type'],
            persona=advisor['persona'],
            title=decision_context.get('title', ''),
            description=decision_context.get('description', ''),
            values=', '.join(decision_context.get('values', [])),
            constraints=str(decision_context.get('constraints', {})),
            scenarios_json=json.dumps(scenarios, indent=2)
        )

        response = await self.llm.ainvoke(messages)
        
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return self._default_perspective(advisor)

    def _default_perspective(self, advisor: Dict[str, str]) -> Dict[str, Any]:
        """Default perspective if LLM parsing fails"""
        perspectives_map = {
            "Pragmatic Parent": {
                "key_concern": "Job security and financial stability for family",
                "recommendation": "Choose the stable job option with proven income",
                "blind_spot_identified": "You might be overlooking your need for growth and fulfillment",
                "questions_to_consider": ["Can you afford to take calculated risks?", "What's your minimum required income?", "How does family depend on this income?"]
            },
            "Risk-Taking Entrepreneur": {
                "key_concern": "Are you maximizing your upside potential?",
                "recommendation": "The startup path offers greatest learning and equity upside",
                "blind_spot_identified": "You might be underestimating your resilience and ability to recover from failure",
                "questions_to_consider": ["What's the worst that could happen and could you recover?", "What's the market opportunity size?", "Do you have a safety net?"]
            },
            "Cautious Academic": {
                "key_concern": "Long-term career trajectory and skill development",
                "recommendation": "Advanced degree provides deepest skill foundation for 10-20 year horizon",
                "blind_spot_identified": "The opportunity cost of delayed earnings might outweigh the degree benefit",
                "questions_to_consider": ["What's the ROI on additional education in your field?", "How quickly do skills become obsolete?", "Can you learn on the job instead?"]
            },
            "Values-First Counselor": {
                "key_concern": "Are you choosing authentically aligned with your true values?",
                "recommendation": "Choose the path that creates most life satisfaction and wellbeing",
                "blind_spot_identified": "You might be letting external expectations override internal compass",
                "questions_to_consider": ["How do you feel when you imagine each path?", "Which aligns best with your authentic self?", "What does success mean to you personally?"]
            },
            "Data-Driven Analyst": {
                "key_concern": "What do the probabilities and data actually suggest?",
                "recommendation": "Analyze the probabilistic outcomes and choose highest expected value",
                "blind_spot_identified": "You might be overweighting narrative and emotion over hard data",
                "questions_to_consider": ["What's the base rate of success for each path?", "What's the mathematical expected value?", "Where is the data uncertainty?"]
            }
        }
        
        default = perspectives_map.get(advisor['type'], {
            "key_concern": "Need more analysis",
            "recommendation": "Requires more information",
            "blind_spot_identified": "Unclear without more context",
            "questions_to_consider": []
        })
        
        return {
            "advisor_type": advisor['type'],
            "key_concern": default.get('key_concern'),
            "recommendation": default.get('recommendation'),
            "blind_spot_identified": default.get('blind_spot_identified'),
            "questions_to_consider": default.get('questions_to_consider', [])
        }
