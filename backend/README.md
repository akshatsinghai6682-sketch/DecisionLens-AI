# DecisionLens AI - Backend

FastAPI backend for DecisionLens AI decision simulator.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=mysql+pymysql://root:password@localhost/decisionlens
DEBUG=True
SECRET_KEY=your_secret_key_here
```

## Database Setup

```bash
mysql -u root -p < schema.sql
```

## Run Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Visit `http://localhost:8000/docs` for interactive API docs (Swagger UI).

## Project Structure

- `app/models/` - SQLAlchemy ORM models
- `app/schemas/` - Pydantic validation schemas
- `app/routes/` - API endpoints
- `app/services/` - Business logic
- `app/agents/` - LangGraph agents
- `app/prompts/` - AI prompt templates
- `app/utils/` - Database and validation utilities

## Testing

```bash
pytest
```
