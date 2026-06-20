"""Report Agent - Generates final clarity report"""

from typing import Dict, List, Any
from langchain.prompts import ChatPromptTemplate
import json


class ReportAgent:
    """Agent responsible for generating final clarity report"""

    def __init__(self, llm):
        self.llm = llm

    async def generate_report(self, decision_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate final clarity report from all analyses"""
        prompt = ChatPromptTemplate.from_template("""
        Synthesize this comprehensive decision analysis into a clear, actionable report.
        
        Analysis:
        - Decision: {decision_title}
        - Scenarios: {scenarios}
        - Tradeoffs: {tradeoffs}
        - Perspectives: {perspectives}
        - Uncertainty: {uncertainty}
        - Financial Analysis: {financial_analysis}
        
        Generate a final clarity report with:
        1. Key Insights: 3-5 major takeaways
        2. Ranked Priorities: What matters most
        3. Main Tradeoffs: The core tensions
        4. Missing Information: What you need to research
        5. Next Research Steps: Specific actions to take
        6. Decision Framework: How to structure your final choice
        7. Gut Check Questions: Questions to ask yourself
        
        Return JSON:
        {{
            "key_insights": ["insight1", "insight2", "insight3"],
            "ranked_priorities": ["priority1", "priority2"],
            "core_tradeoffs": ["tradeoff1", "tradeoff2"],
            "missing_information": ["info1", "info2"],
            "next_research_steps": ["step1", "step2", "step3"],
            "decision_framework": "Suggested framework for making final choice",
            "gut_check_questions": ["question1", "question2", "question3"],
            "confidence_in_clarity": 0.0-1.0
        }}
        
        Return ONLY valid JSON, no other text.
        """)

        messages = prompt.format_messages(
            decision_title=decision_analysis.get('decision_title', ''),
            scenarios=json.dumps(decision_analysis.get('scenarios', []), indent=2),
            tradeoffs=json.dumps(decision_analysis.get('tradeoffs', []), indent=2),
            perspectives=json.dumps(decision_analysis.get('perspectives', []), indent=2),
            uncertainty=json.dumps(decision_analysis.get('uncertainty', {}), indent=2),
            financial_analysis=json.dumps(decision_analysis.get('financial_analysis', {}), indent=2)
        )

        response = await self.llm.ainvoke(messages)
        
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return self._default_report()

    def _default_report(self) -> Dict[str, Any]:
        """Default report if LLM parsing fails"""
        return {
            "key_insights": [
                "Each path has distinct tradeoffs - no clear winner",
                "Your values should guide more than financial metrics",
                "Risk tolerance is the key differentiator between paths"
            ],
            "ranked_priorities": [
                "Alignment with personal values (critical)",
                "Financial sustainability (important)",
                "Career growth potential (important)",
                "Lifestyle quality (important)"
            ],
            "core_tradeoffs": [
                "Stability vs. Growth: Job provides stability; startup offers growth",
                "Short-term income vs. Long-term trajectory: Degree delays income but increases ceiling",
                "Geographic flexibility vs. Community: Each path has different location implications"
            ],
            "missing_information": [
                "Specific startup team dynamics and market validation",
                "Detailed program outcomes and alumni career paths",
                "Company culture and growth opportunity details"
            ],
            "next_research_steps": [
                "Interview people 5 years into each path",
                "Validate startup business model with customers",
                "Research program ROI and career outcomes",
                "Explore options for combining paths (e.g., job while studying)"
            ],
            "decision_framework": "1) Eliminate options that violate core values. 2) Evaluate remaining by financial sustainability. 3) Choose based on which scenario you're most excited to work toward. 4) Set decision deadline. 5) Build contingency plans.",
            "gut_check_questions": [
                "Which path makes you most energized when you imagine it?",
                "Which would you most regret not trying?",
                "What are you actually afraid of in each option?",
                "Who do you want to become?"
            ],
            "confidence_in_clarity": 0.75
        }
