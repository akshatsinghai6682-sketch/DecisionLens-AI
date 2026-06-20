# DecisionLens AI - Architecture Document

## Overview

DecisionLens AI is a multi-agent system that helps users make complex life decisions by simulating scenarios, identifying hidden tradeoffs, and providing diverse perspectives.

## System Architecture

### Frontend
- React + TypeScript
- Vite build tool
- Tailwind CSS for styling
- React Context for state management
- React Router for navigation
- Recharts for data visualization

### Backend
- FastAPI for REST API
- SQLAlchemy ORM with MySQL
- LangGraph for agent orchestration
- Google Gemini API for AI
- ReportLab for PDF generation

### Database
- Local MySQL (MVP)
- 7 tables: users, decisions, decision_contexts, scenarios, advisor_perspectives, tradeoffs, sessions

## Multi-Agent System Flow

```
User Input (Decision) → Facilitator Agent
                          ↓
                    Diagnostic Questions
                          ↓
                    User Profile Built
                          ↓
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
   Tradeoff         Scenario              Perspective
   Discovery Agent  Simulator Agent       Panel Agent
        ↓                 ↓                 ↓
   Hidden Tradeoffs  3 Scenarios          5 Advisors
        ↓                 ↓                 ↓
        └─────────────────┼─────────────────┘
                          ↓
                  Financial Analyst Agent
                          ↓
                  Uncertainty Agent
                          ↓
                    Report Agent
                          ↓
                  Final Clarity Report
```

## API Structure

### Authentication (Mock)
- POST /auth/signin - Mock sign-in
- POST /auth/signup - Mock user creation

### Decisions
- POST /decisions - Create decision
- GET /decisions - List user decisions
- GET /decisions/{id} - Get decision details
- PATCH /decisions/{id} - Update decision

### Chat & Diagnostics
- POST /chat/send - Send chat message
- GET /chat/{session_id} - Get session history

### Scenarios
- GET /decisions/{id}/scenarios - Get decision scenarios
- POST /decisions/{id}/scenarios/generate - Trigger scenario generation

### Reports
- GET /decisions/{id}/report - Get clarity report
- POST /decisions/{id}/report/export-pdf - Export as PDF

## Key Design Decisions

1. **Offline-First MVP**: Only Gemini API is real. Everything else is local for rapid development.

2. **Mock Authentication**: Uses localStorage for session management. No real auth system in MVP.

3. **Multi-Agent Orchestration**: LangGraph enables parallel processing of different analysis aspects.

4. **Responsible AI by Design**: Confidence levels, alternative perspectives, and uncertainty mapping are built-in.

5. **Modular Structure**: Each agent can be tested and improved independently.

## Data Flow

### Decision Creation
1. User submits decision title + description
2. Backend stores decision record
3. Creates session for conversation

### Diagnostic Phase
1. Facilitator Agent asks 5 questions
2. User answers collected
3. User profile built from responses
4. Decision context saved

### Analysis Phase
1. Tradeoff Discovery identifies hidden tradeoffs
2. Scenario Simulator generates 3 scenarios (best/expected/worst)
3. Perspective Panel generates 5 advisor perspectives
4. Financial Analyst scores financial impact
5. Uncertainty Agent maps known/unknown factors

### Report Phase
1. Report Agent synthesizes all analysis
2. Generates final clarity report
3. Exports as PDF with visualizations

## Security Considerations (MVP)

- All data stored locally (no cloud)
- No authentication required (mock only)
- No PII transmitted to external services
- Environment variables for API keys
- CORS configured for localhost only

## Performance Optimizations

- Connection pooling for database
- Async/await for I/O operations
- Response caching for scenario comparisons
- Lazy loading of visualizations

## Scalability Notes

This MVP is designed for development. For production:
- Add real authentication
- Migrate to cloud database
- Implement caching layer
- Add job queue for long-running operations
- Implement rate limiting
