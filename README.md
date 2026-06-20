# DecisionLens AI 🧠💡

> Your AI-Powered Life Decision Simulator for Complex Choices

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![React](https://img.shields.io/badge/react-18%2B-blue)
![Status](https://img.shields.io/badge/status-Active%20Development-green)

## 🎯 Overview

DecisionLens AI is a full-stack application that helps you make better life decisions by:

1. **Understanding Your Context** - Diagnostic chat to understand your values, constraints, and vision
2. **Perspective Panel** - 5 AI advisor archetypes offer diverse viewpoints
3. **Scenario Simulation** - Explore best, expected, and worst-case outcomes
4. **Hidden Tradeoffs** - Discover non-obvious consequences
5. **Uncertainty Mapping** - Understand what you know, don't know, and are assuming
6. **Clarity Report** - Export comprehensive PDF analysis

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Frontend (React + TS)           │
│  ├─ Landing Page                        │
│  ├─ Diagnostic Chat Interface           │
│  ├─ Advisor Perspective Panel           │
│  ├─ Scenario Comparison Views           │
│  └─ Clarity Report Generator            │
└────────────────────┬────────────────────┘
                     │ REST API
┌────────────────────▼─────────────���──────┐
│      Backend API (FastAPI)              │
│  ├─ Auth Service                        │
│  ├─ Decision Service                    │
│  ├─ Chat Service                        │
│  ├─ Scenario Service                    │
│  ├─ Report Service                      │
│  └─ PDF Generation Service              │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│      AI Orchestration Layer             │
│  ├─ LangGraph Workflow Manager          │
│  ├─ Multi-Agent Coordinator             │
│  ├─ Prompt Templates                    │
│  └─ Context Manager                     │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│    Google Gemini AI (API)               │
│  ├─ Diagnostic Questions                │
│  ├─ Advisor Perspectives                │
│  ├─ Scenario Generation                 │
│  └─ Tradeoff Discovery                  │
└─────────────────────────────────────────┘
```

## 📦 Tech Stack

### Backend
- **Framework**: FastAPI 0.104+
- **Language**: Python 3.10+
- **AI/LLM**: Google Gemini API
- **Workflow**: LangGraph
- **Database**: PostgreSQL (optional), SQLite for local
- **PDF**: ReportLab
- **Async**: AsyncIO, Uvicorn

### Frontend
- **Framework**: React 18+
- **Language**: TypeScript 5+
- **Styling**: Tailwind CSS
- **State**: Context API
- **Charts**: Recharts
- **Icons**: Lucide React
- **Build**: Vite

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Google Gemini API key (free at https://makersuite.google.com/app/apikey)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Start server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install

# Configure environment
cp .env.example .env.local
# Edit .env.local if needed

# Start dev server
npm start
```

### Access Application
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs

## 📋 Features

### Phase 1: Landing & Auth
- ✅ Landing page with feature overview
- ✅ User authentication system
- ✅ User profiles

### Phase 2-3: Diagnostic Chat
- ✅ 5 diagnostic questions about decision context
- ✅ AI-powered follow-up questions
- ✅ Context accumulation

### Phase 4-5: Advisor Perspectives
- ✅ 5 advisor archetypes (Pragmatic Parent, Risk-Taking Entrepreneur, etc.)
- ✅ Unique perspectives from each advisor
- ✅ Blind spot identification

### Phase 6-7: Scenario Simulation
- ✅ Best case scenario generation
- ✅ Expected case scenario
- ✅ Worst case scenario
- ✅ Scenario comparison visualizations
- ✅ Financial impact analysis

### Phase 8-9: Hidden Tradeoffs & Uncertainty
- ✅ Tradeoff discovery and acknowledgment
- ✅ Uncertainty mapping (known/unknown/assumptions)
- ✅ Key factors identification

### Phase 10: Clarity Report
- ✅ Comprehensive PDF report generation
- ✅ Key insights summary
- ✅ Ranked priorities
- ✅ Decision framework
- ✅ Gut check questions

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```env
GEMINI_API_KEY=your_api_key
DATABASE_URL=sqlite:///./test.db
DEBUG=True
```

**Frontend (.env.local)**
```env
REACT_APP_API_URL=http://localhost:8000
```

## 📚 API Endpoints

### Authentication
- `POST /auth/signin` - Sign in user
- `POST /auth/signup` - Create new user
- `GET /auth/users` - List all users

### Decisions
- `POST /decisions/` - Create new decision
- `GET /decisions/{id}` - Get decision details
- `GET /decisions/user/{user_id}` - List user decisions
- `PATCH /decisions/{id}/context` - Update decision context

### Chat
- `GET /chat/questions` - Get diagnostic questions
- `POST /chat/start-session` - Start chat session
- `POST /chat/send` - Send message
- `GET /chat/session/{session_id}` - Get chat history

### Scenarios
- `GET /scenarios/decision/{decision_id}` - List scenarios
- `POST /scenarios/decision/{decision_id}/generate` - Generate scenarios

### Reports
- `GET /reports/decision/{decision_id}` - Get report
- `POST /reports/decision/{decision_id}/export-pdf` - Export as PDF

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest
pytest --cov=app  # With coverage

# Frontend tests
cd frontend
npm test
npm test -- --coverage
```

See [TESTING.md](TESTING.md) for detailed testing guide.

## 📖 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment instructions including:
- Docker setup
- Cloud deployment (AWS, GCP, Azure)
- Database configuration
- Performance optimization
- Security checklist

## 🎓 Project Context

**Built for**: USAII Global AI Hackathon 2026
**Track**: Undergraduate
**Challenge**: Challenge 3 - AI-Powered Application

## 📂 Project Structure

```
DecisionLens-AI/
├── backend/
│   ├── app/
│   │   ├── agents/              # AI agents for each phase
│   │   ├── services/            # Business logic services
│   │   ├── models/              # Data models
│   │   ├── prompts/             # LLM prompt templates
│   │   ├── routers/             # API endpoints
│   │   ├── orchestration/       # LangGraph workflows
│   │   ├── schemas/             # Request/response schemas
│   │   └── main.py              # FastAPI app
│   ├── tests/                   # Test suite
│   ├── requirements.txt          # Python dependencies
│   └── .env.example              # Environment template
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   │   ├── common/
│   │   │   ├── chat/
│   │   │   ├── advisor/
│   │   │   ├── decision/
│   │   │   ├── visualization/
│   │   │   └── report/
│   │   ├── context/             # React Context
│   │   ├── hooks/               # Custom hooks
│   │   ├── utils/               # Utilities
│   │   ├── pages/               # Page components
│   │   └── App.tsx              # Main app
│   ├── tests/                   # Test suite
│   ├── package.json
│   └── .env.example
├── DEPLOYMENT.md                # Deployment guide
├── TESTING.md                   # Testing guide
└── README.md                    # This file
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## ⚖️ License

MIT License - See LICENSE file for details

## 📞 Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Documentation**: See README and deployment guide

## 🙏 Acknowledgments

- Built with ❤️ for the USAII Global AI Hackathon 2026
- Powered by Google Gemini API
- Special thanks to the React and FastAPI communities

---

**Remember**: DecisionLens AI is a decision aid, not a decision maker. You are responsible for your final choice. 🎯
