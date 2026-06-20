# DecisionLens AI - Testing Guide

## Test Structure

```
backend/
  tests/
    unit/
      test_services.py
      test_agents.py
      test_models.py
    integration/
      test_api_endpoints.py
      test_workflow.py
    fixtures/
      conftest.py

frontend/
  src/
    __tests__/
      components/
      hooks/
      utils/
```

## Backend Testing

### Setup

```bash
cd backend
pip install pytest pytest-asyncio pytest-cov
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_services.py

# Run with coverage
pytest --cov=app tests/

# Run with verbose output
pytest -v

# Run only unit tests
pytest tests/unit/

# Run only integration tests
pytest tests/integration/
```

### Example Test

```python
import pytest
from app.services.decision_service import DecisionService

@pytest.mark.asyncio
async def test_create_decision():
    service = DecisionService()
    decision = await service.create(
        user_id="test-user",
        title="Test Decision",
        description="A test decision"
    )
    assert decision.id is not None
    assert decision.title == "Test Decision"
    assert decision.status == "in_progress"
```

## Frontend Testing

### Setup

```bash
cd frontend
npm install --save-dev @testing-library/react @testing-library/jest-dom vitest
```

### Running Tests

```bash
# Run all tests
npm test

# Run specific test file
npm test -- ChatInterface.test.tsx

# Run with coverage
npm test -- --coverage

# Watch mode
npm test -- --watch
```

### Example Component Test

```typescript
import { render, screen } from '@testing-library/react';
import { ChatInterface } from '@/components/chat/ChatInterface';

describe('ChatInterface', () => {
  it('renders messages correctly', () => {
    const messages = [
      { role: 'user', content: 'Hello', timestamp: '2024-01-01' },
      { role: 'assistant', content: 'Hi there!', timestamp: '2024-01-01' }
    ];
    
    render(
      <ChatInterface
        messages={messages}
        onSendMessage={jest.fn()}
      />
    );
    
    expect(screen.getByText('Hello')).toBeInTheDocument();
    expect(screen.getByText('Hi there!')).toBeInTheDocument();
  });
});
```

## API Testing

### Using curl

```bash
# Test auth endpoint
curl -X POST http://localhost:8000/auth/signin \
  -H "Content-Type: application/json" \
  -d '{"user_id": "test-user", "user_name": "Test User"}'

# Test decision creation
curl -X POST http://localhost:8000/decisions?user_id=test-user \
  -H "Content-Type: application/json" \
  -d '{"title": "Should I move?", "description": "Considering relocating"}'
```

### Using Postman

1. Import Postman collection from `postman_collection.json`
2. Set environment variables (API_URL, USER_ID)
3. Run requests against local/staging/production

## Performance Testing

### Load Testing with Locust

```python
from locust import HttpUser, task, between

class DecisionLensUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_questions(self):
        self.client.get("/chat/questions")
    
    @task
    def create_decision(self):
        self.client.post(
            "/decisions",
            json={"title": "Test", "description": "Test"}
        )
```

```bash
locust -f tests/load/locustfile.py --host=http://localhost:8000
```

## E2E Testing

### Setup Cypress

```bash
npm install --save-dev cypress
npx cypress open
```

### Example E2E Test

```typescript
describe('Decision Flow', () => {
  it('completes full decision flow', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Start Decision').click()
    cy.get('input[type="text"]').type('Should I change jobs?')
    cy.contains('Next').click()
    // ... more steps
  })
})
```

## Test Coverage Goals

- Backend: 80%+ coverage
- Frontend: 70%+ coverage
- Critical paths: 95%+ coverage

## Continuous Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r backend/requirements.txt
      - run: pytest backend/tests/
  
  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - run: cd frontend && npm install
      - run: npm test
```

## Debugging Tests

### Backend

```bash
# Run with pdb debugger
pytest --pdb

# Set breakpoint in code
import pdb; pdb.set_trace()
```

### Frontend

```bash
# Debug in VS Code
# Add to .vscode/launch.json:
{
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/node_modules/.bin/jest"
}
```
