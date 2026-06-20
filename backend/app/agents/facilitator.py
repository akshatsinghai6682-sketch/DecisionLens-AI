"""Facilitator Agent - Guides conversation and builds user profile"""

from typing import Dict, List, Any
from langchain.prompts import ChatPromptTemplate
from app.schemas.decision import DecisionContextUpdate


class FacilitatorAgent:
    """Agent responsible for guiding the diagnostic conversation"""

    def __init__(self, llm):
        self.llm = llm
        self.diagnostic_questions = [
            {
                "category": "values",
                "question": "What are your top 3 personal values that matter most to you in making this decision?",
                "examples": "e.g., financial security, personal growth, family time, impact on society, creativity"
            },
            {
                "category": "constraints",
                "question": "What are your key constraints? (e.g., location, family obligations, health, financial situation)",
                "examples": "e.g., must stay in current city, have dependents, limited savings, time constraints"
            },
            {
                "category": "timeline",
                "question": "What's your time horizon for this decision? When do you need to decide?",
                "examples": "e.g., immediately, within 3 months, within a year, long-term planning"
            },
            {
                "category": "financial",
                "question": "Describe your current financial situation and what matters to you financially.",
                "examples": "e.g., no savings, stable job, have debt, need minimum income, flexibility more important"
            },
            {
                "category": "risk",
                "question": "How comfortable are you with risk? What would be unacceptable outcomes?",
                "examples": "e.g., very risk-averse, comfortable with uncertainty, must have safety net, prefer stability"
            }
        ]

    def get_diagnostic_questions(self) -> List[Dict[str, str]]:
        """Return list of diagnostic questions"""
        return self.diagnostic_questions

    def get_next_question(self, question_index: int) -> Dict[str, str]:
        """Get next diagnostic question"""
        if 0 <= question_index < len(self.diagnostic_questions):
            return self.diagnostic_questions[question_index]
        return None

    async def build_user_profile(self, answers: Dict[str, str]) -> DecisionContextUpdate:
        """Build user profile from diagnostic answers"""
        prompt = ChatPromptTemplate.from_template("""
        Based on the user's answers to diagnostic questions, create a structured user profile.
        
        Answers:
        - Values: {values_answer}
        - Constraints: {constraints_answer}
        - Timeline: {timeline_answer}
        - Financial: {financial_answer}
        - Risk Tolerance: {risk_answer}
        
        Generate a JSON response with:
        - top_values: [list of top values]
        - constraints: {{constraint_type: description}}
        - timeline: "short_term"|"medium_term"|"long_term"
        - financial_situation: brief description
        - risk_tolerance: "low"|"medium"|"high"
        
        Return ONLY valid JSON, no other text.
        """)

        messages = prompt.format_messages(
            values_answer=answers.get('values', ''),
            constraints_answer=answers.get('constraints', ''),
            timeline_answer=answers.get('timeline', ''),
            financial_answer=answers.get('financial', ''),
            risk_answer=answers.get('risk', '')
        )

        response = await self.llm.ainvoke(messages)
        
        # Parse response and return DecisionContextUpdate
        import json
        try:
            profile_data = json.loads(response.content)
            return DecisionContextUpdate(
                values_profile=profile_data.get('top_values', []),
                constraints=profile_data.get('constraints', {}),
                timeline=profile_data.get('timeline'),
                financial_situation=profile_data.get('financial_situation'),
                risk_tolerance=profile_data.get('risk_tolerance')
            )
        except json.JSONDecodeError:
            return DecisionContextUpdate()

    def validate_answer(self, answer: str) -> bool:
        """Validate user answer"""
        return len(answer.strip()) >= 10 and len(answer.strip()) <= 2000
