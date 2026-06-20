# DecisionLens AI

**An AI-powered life decision simulator and second-opinion reasoning system**

Built for USAII Global AI Hackathon 2026 - Undergraduate Track Challenge 3 (Second Brain for Real Life)

## Vision

Most decision tools generate pros and cons. DecisionLens AI helps users:

- Think clearly about complex decisions
- Identify hidden tradeoffs and blind spots
- Compare multiple scenarios with uncertainty modeling
- Understand different perspectives on their situation
- Make informed decisions (humans always decide, never the AI)

## Tech Stack

**Frontend**: React + TypeScript + Tailwind CSS + ShadCN UI + Recharts
**Backend**: FastAPI + Python
**AI**: Gemini API + LangGraph + LangChain
**Database**: Local MySQL + SQLAlchemy ORM
**PDF**: ReportLab
**State**: React Context

## Features

✅ Structured decision intake & diagnostic conversation
✅ Hidden tradeoff discovery
✅ Multi-scenario simulation with financial/career/lifestyle analysis
✅ Perspective panel (5 advisor archetypes)
✅ Uncertainty mapping (known vs unknown factors)
✅ Interactive visualizations (Recharts)
✅ PDF clarity report generation
✅ Responsible AI guardrails & disclaimers

## Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set up local MySQL database
mysql -u root -p < schema.sql

# Start server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000`

## Project Structure

```
DecisionLens-AI/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── decision.py
│   │   │   ├── scenario.py
│   │   │   ├── tradeoff.py
│   │   │   └── session.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── decision.py
│   │   │   ├── scenario.py
│   │   │   └── advisor.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── decisions.py
│   │   │   ├── chat.py
│   │   │   ├── scenarios.py
│   │   │   ├── reports.py
│   │   │   └── health.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── decision_service.py
│   │   │   ├── scenario_service.py
│   │   │   ├── report_service.py
│   │   │   └── pdf_service.py
│   │   ���── agents/
│   │   │   ├── __init__.py
│   │   │   ├── facilitator.py
│   │   │   ├── tradeoff_discovery.py
│   │   │   ├── scenario_simulator.py
│   │   │   ├── financial_analyst.py
│   │   │   ├── perspective_panel.py
│   │   │   ├── uncertainty_agent.py
│   │   │   └── report_agent.py
│   │   ├── prompts/
│   │   │   ├── __init__.py
│   │   │   ├── facilitator_prompts.py
│   │   │   ├── tradeoff_prompts.py
│   │   │   ├── scenario_prompts.py
│   │   │   ├── financial_prompts.py
│   │   │   ├── perspective_prompts.py
│   │   │   ├── uncertainty_prompts.py
│   │   │   └── report_prompts.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── db.py
│   │       └── validators.py
│   ├── requirements.txt
│   ├── schema.sql
│   ├── .env.example
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── Footer.tsx
│   │   │   │   ├── Disclaimer.tsx
│   │   │   │   └── LoadingSpinner.tsx
│   │   │   ├── decision/
│   │   │   │   ├── DecisionInput.tsx
│   │   │   │   ├── TradeoffCard.tsx
│   │   │   │   └── ScenarioComparison.tsx
│   │   │   ├── chat/
│   │   │   │   ├── ChatInterface.tsx
│   │   │   │   ├── QuestionCard.tsx
│   │   │   │   └── AnswerInput.tsx
│   │   │   ├── visualization/
│   │   │   │   ├── RadarChart.tsx
│   │   │   │   ├── ConfidenceMeter.tsx
│   │   │   │   └── ComparisonChart.tsx
│   │   │   ├── advisor/
│   │   │   │   ├── AdvisorCard.tsx
│   │   │   │   └── PerspectivePanel.tsx
│   │   │   └── report/
│   │   │       ├── ClarityReport.tsx
│   │   │       └── UncertaintyMap.tsx
│   │   ├── pages/
│   │   │   ├── Landing.tsx
│   │   │   ├── DecisionIntake.tsx
│   │   │   ├── DiagnosticChat.tsx
│   │   │   ├── TradeoffReview.tsx
│   │   │   ├── ScenarioSimulation.tsx
│   │   │   ├── PerspectiveView.tsx
│   │   │   ├── UncertaintyView.tsx
│   │   │   └── ClarityReportView.tsx
│   │   ├── hooks/
│   │   │   ├── useDecision.ts
│   │   │   ├── useChat.ts
│   │   │   ├── useScenarios.ts
│   │   │   └── useReport.ts
│   │   ├── context/
│   │   │   ├── DecisionContext.tsx
│   │   │   ├── UserContext.tsx
│   │   │   └── UIContext.tsx
│   │   ├── utils/
│   │   │   ├── api.ts
│   │   │   ├── constants.ts
│   │   │   └── localStorage.ts
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_ENDPOINTS.md
│   ├── AGENT_WORKFLOW.md
│   ├── DATABASE_SCHEMA.md
│   └── DEPLOYMENT.md
├── .gitignore
└── README.md
```

## User Flow

1. **Landing** → Describe decision (e.g., "Master's degree, job, or startup?")
2. **Diagnostic Chat** → AI asks 5 questions (values, constraints, timeline, finances, risk)
3. **Tradeoff Review** → AI surfaces 3-5 hidden tradeoffs
4. **Scenario Simulation** → AI generates 3 scenarios with detailed analysis
5. **Perspective Panel** → 5 advisor archetypes provide viewpoints
6. **Uncertainty Map** → Known vs unknown factors displayed
7. **Clarity Report** → Exportable PDF with key insights

## Multi-Agent System (LangGraph)

- **Facilitator Agent**: Guides conversation, builds user profile
- **Tradeoff Discovery Agent**: Identifies blind spots and hidden tradeoffs
- **Scenario Simulation Agent**: Models best/expected/worst cases
- **Financial Analyst Agent**: Salary, cost of living, ROI analysis
- **Perspective Panel Agent**: 5 distinct advisor personas
- **Uncertainty Agent**: Maps confidence and missing info
- **Report Agent**: Generates final clarity report

## Responsible AI

✅ Never prescribes decisions ("You should choose X")
✅ Always shows confidence levels and assumptions
✅ Displays missing information gaps
✅ Highlights uncertainty and biases
✅ Emphasizes human agency in final decision
✅ Shows alternative perspectives automatically

## Deployment (MVP)

- **Development**: Localhost only
- **Database**: Local MySQL
- **Auth**: Mock sign-in with localStorage
- **No external services**: This is offline-first MVP

## Team & Timeline

**Team Size**: 3 students
**Duration**: 7 days
**Target**: Production-quality MVP

## Database Schema

- `users` - Mock user accounts (localStorage)
- `decisions` - Decision records with metadata
- `decision_context` - Values, constraints, risk profiles
- `scenarios` - Simulation results with scoring
- `tradeoffs` - Hidden tradeoffs discovered
- `sessions` - Chat conversation history
- `advisor_perspectives` - Perspective panel outputs

## 10-Phase Build Plan

✅ Phase 1: Project structure
→ Phase 2: Backend architecture
→ Phase 3: Database models
→ Phase 4: LangGraph agent architecture
→ Phase 5: API endpoints
→ Phase 6: Frontend architecture
→ Phase 7: React components
→ Phase 8: Prompt templates
→ Phase 9: PDF generation
→ Phase 10: Deployment instructions

## License

MIT

## Contact

Built for USAII Hackathon 2026
