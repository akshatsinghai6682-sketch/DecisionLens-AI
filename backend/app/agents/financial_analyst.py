"""Financial Analyst Agent - Analyzes financial impact"""

from typing import Dict, Any
from langchain.prompts import ChatPromptTemplate
import json


class FinancialAnalystAgent:
    """Agent responsible for financial analysis and scoring"""

    def __init__(self, llm):
        self.llm = llm

    async def analyze_financial_impact(self, decision_context: Dict[str, Any], scenarios: list) -> Dict[str, Any]:
        """Analyze financial impact across scenarios"""
        prompt = ChatPromptTemplate.from_template("""
        Analyze the financial impact of these decision scenarios.
        
        Decision: {title}
        Description: {description}
        User's Financial Situation: {financial_situation}
        Timeline: {timeline}
        
        Scenarios to analyze:
        {scenarios_json}
        
        Provide financial analysis including:
        1. Expected income trajectory
        2. Major expenses (education, relocation, etc)
        3. Cost of living impact
        4. Time to financial stability
        5. Long-term wealth implications
        6. Financial risk factors
        
        Return JSON:
        {{
            "analysis": "Summary of financial implications",
            "income_projection": "Expected income over 5 years",
            "major_costs": ["cost1", "cost2"],
            "break_even_timeline": "months or years",
            "financial_risks": ["risk1", "risk2"],
            "financial_opportunities": ["opp1", "opp2"]
        }}
        
        Return ONLY valid JSON, no other text.
        """)

        messages = prompt.format_messages(
            title=decision_context.get('title', ''),
            description=decision_context.get('description', ''),
            financial_situation=decision_context.get('financial_situation', ''),
            timeline=decision_context.get('timeline', ''),
            scenarios_json=json.dumps(scenarios, indent=2)
        )

        response = await self.llm.ainvoke(messages)
        
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return self._default_financial_analysis()

    def _default_financial_analysis(self) -> Dict[str, Any]:
        """Default financial analysis if LLM parsing fails"""
        return {
            "analysis": "Financial impact varies significantly based on chosen path. Consider both immediate costs and long-term trajectory.",
            "income_projection": "Varies by scenario. Startup high-risk, job stable, education delayed but higher growth.",
            "major_costs": ["Education costs if applicable", "Relocation expenses", "Opportunity cost of time"],
            "break_even_timeline": "2-5 years depending on path",
            "financial_risks": ["Market volatility", "Income uncertainty", "Hidden expenses"],
            "financial_opportunities": ["Equity upside if startup", "Salary growth trajectory", "Skill development ROI"]
        }
