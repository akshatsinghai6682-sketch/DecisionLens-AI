"""LangGraph agent orchestration - Multi-agent workflow"""

from typing import Dict, Any, List
from langchain_google_genai import ChatGoogleGenerativeAI
from app.agents.facilitator import FacilitatorAgent
from app.agents.tradeoff_discovery import TradeoffDiscoveryAgent
from app.agents.scenario_simulator import ScenarioSimulatorAgent
from app.agents.financial_analyst import FinancialAnalystAgent
from app.agents.perspective_panel import PerspectivePanelAgent
from app.agents.uncertainty_agent import UncertaintyAgent
from app.agents.report_agent import ReportAgent
from app.config import settings


class DecisionOrchestratorLangGraph:
    """Orchestrates multi-agent workflow using LangGraph pattern"""

    def __init__(self):
        """Initialize all agents"""
        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=settings.TEMPERATURE,
        )

        # Initialize agents
        self.facilitator = FacilitatorAgent(self.llm)
        self.tradeoff_discovery = TradeoffDiscoveryAgent(self.llm)
        self.scenario_simulator = ScenarioSimulatorAgent(self.llm)
        self.financial_analyst = FinancialAnalystAgent(self.llm)
        self.perspective_panel = PerspectivePanelAgent(self.llm)
        self.uncertainty_agent = UncertaintyAgent(self.llm)
        self.report_agent = ReportAgent(self.llm)

    async def run_decision_analysis(self, decision_context: Dict[str, Any]) -> Dict[str, Any]:
        """Run complete decision analysis workflow"""
        
        print("[Orchestrator] Starting decision analysis...")
        
        # Phase 1: Tradeoff Discovery (parallel)
        print("[Orchestrator] Phase 1: Discovering tradeoffs...")
        tradeoffs = await self.tradeoff_discovery.discover_tradeoffs(decision_context)
        
        # Phase 2: Scenario Simulation (parallel)
        print("[Orchestrator] Phase 2: Simulating scenarios...")
        scenarios = await self.scenario_simulator.generate_scenarios(decision_context)
        
        # Phase 3: Perspective Panel (parallel)
        print("[Orchestrator] Phase 3: Gathering perspectives...")
        perspectives = await self.perspective_panel.generate_perspectives(decision_context, scenarios)
        
        # Phase 4: Financial Analysis (uses scenarios)
        print("[Orchestrator] Phase 4: Analyzing financial impact...")
        financial_analysis = await self.financial_analyst.analyze_financial_impact(
            decision_context,
            scenarios
        )
        
        # Phase 5: Uncertainty Mapping (uses scenarios)
        print("[Orchestrator] Phase 5: Mapping uncertainty...")
        uncertainty_map = await self.uncertainty_agent.map_uncertainty(
            decision_context,
            scenarios
        )
        
        # Phase 6: Generate Final Report (synthesizes all)
        print("[Orchestrator] Phase 6: Generating final report...")
        analysis_summary = {
            "decision_title": decision_context.get('title', ''),
            "scenarios": scenarios,
            "tradeoffs": tradeoffs,
            "perspectives": perspectives,
            "uncertainty": uncertainty_map,
            "financial_analysis": financial_analysis
        }
        
        final_report = await self.report_agent.generate_report(analysis_summary)
        
        print("[Orchestrator] Analysis complete!")
        
        return {
            "decision_context": decision_context,
            "tradeoffs": tradeoffs,
            "scenarios": scenarios,
            "perspectives": perspectives,
            "financial_analysis": financial_analysis,
            "uncertainty_map": uncertainty_map,
            "final_report": final_report
        }

    def get_diagnostic_questions(self) -> List[Dict[str, str]]:
        """Get diagnostic questions from facilitator"""
        return self.facilitator.get_diagnostic_questions()
