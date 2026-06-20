# DecisionLens AI - Deployment Guide

## Overview

DecisionLens AI is a full-stack application built with:
- **Backend**: FastAPI + Python
- **Frontend**: React + TypeScript
- **AI Engine**: Google Gemini API
- **Database**: PostgreSQL (optional, for production)
- **PDF Generation**: ReportLab

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn
- Google Gemini API key (free at https://makersuite.google.com/app/apikey)
- (Optional) PostgreSQL 12+
- (Optional) Docker & Docker Compose

## Quick Start (Local Development)

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-pdf.txt

# Set environment variables
cp .env.example .env
# Edit .env and add your Google Gemini API key

# Run migrations (if using database)
alembic upgrade head

# Start backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local
# Edit .env.local and set REACT_APP_API_URL=http://localhost:8000

# Start development server
npm start
```

### 3. Verify Installation

- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:3000

## Environment Variables

### Backend (.env)

```env
# Google Gemini API
GEMINI_API_KEY=your_api_key_here

# Database (optional)
DATABASE_URL=postgresql://user:password@localhost:5432/decisionlens

# API Settings
API_TITLE=DecisionLens API
API_VERSION=1.0.0
DEBUG=True

# CORS Settings
CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]
```

### Frontend (.env.local)

```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENVIRONMENT=development
```

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and start all services
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Compose File Structure

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/decisionlens
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://backend:8000

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=decisionlens
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Production Deployment

### Backend (Using Gunicorn + Nginx)

1. **Build Production Image**
   ```bash
   docker build -f backend/Dockerfile -t decisionlens-backend:latest .
   ```

2. **Deploy to Cloud Platform**
   - AWS ECS
   - Google Cloud Run
   - Azure Container Instances
   - Heroku
   - DigitalOcean App Platform

3. **Example Gunicorn Command**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
   ```

### Frontend (Using Nginx)

1. **Build Production Bundle**
   ```bash
   npm run build
   ```

2. **Nginx Configuration**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           root /usr/share/nginx/html;
           index index.html index.htm;
           try_files $uri $uri/ /index.html;
       }
       
       location /api {
           proxy_pass http://backend:8000;
       }
   }
   ```

3. **Deploy Static Build**
   - S3 + CloudFront (AWS)
   - Cloud Storage + CDN (Google Cloud)
   - Netlify
   - Vercel

## Database Setup (PostgreSQL)

### Initialize Database

```bash
# Create database
creatdb decisionlens

# Run migrations
alembic upgrade head

# Seed initial data (if needed)
python -m app.scripts.seed_data
```

### Connection String

```
postgresql://username:password@host:5432/decisionlens
```

## API Documentation

Once backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Performance Optimization

### Backend
- Enable caching with Redis
- Use connection pooling
- Implement rate limiting
- Add request logging
- Monitor API response times

### Frontend
- Enable code splitting
- Lazy load components
- Minify and compress assets
- Use CDN for static files
- Implement service workers for offline support

## Monitoring & Logging

### Backend
- Sentry for error tracking
- CloudWatch for logs
- Prometheus for metrics
- New Relic for APM

### Frontend
- Google Analytics
- Sentry for client errors
- LogRocket for session replay

## SSL/TLS Certificate

```bash
# Using Let's Encrypt with Certbot
sudo certbot certonly --standalone -d yourdomain.com

# Auto-renewal
sudo certbot renew --dry-run
```

## Security Checklist

- [ ] Set CORS properly
- [ ] Implement authentication/authorization
- [ ] Use HTTPS only
- [ ] Sanitize user inputs
- [ ] Set up rate limiting
- [ ] Use environment variables for secrets
- [ ] Enable CSRF protection
- [ ] Implement API key authentication
- [ ] Regular security audits
- [ ] Keep dependencies updated

## Troubleshooting

### Backend Issues

**Issue**: `ModuleNotFoundError: No module named 'app'`
- Solution: Ensure you're in the backend directory and virtual environment is activated

**Issue**: `GEMINI_API_KEY not found`
- Solution: Check .env file and ensure API key is set

**Issue**: Database connection error
- Solution: Verify DATABASE_URL is correct and PostgreSQL is running

### Frontend Issues

**Issue**: `REACT_APP_API_URL is undefined`
- Solution: Check .env.local file and restart dev server

**Issue**: CORS errors
- Solution: Ensure backend CORS_ORIGINS includes frontend URL

**Issue**: API requests failing
- Solution: Check backend is running and API_URL is correct in .env.local

## Scaling Strategy

### Phase 1: Basic Deployment
- Single server for backend
- Static hosting for frontend
- SQLite or small PostgreSQL instance

### Phase 2: Growth
- Load balancer
- Multiple backend instances
- Redis caching
- CDN for frontend

### Phase 3: Enterprise
- Kubernetes cluster
- Auto-scaling groups
- RDS database with replication
- CloudFront distribution
- API Gateway

## Support & Resources

- **Documentation**: See README.md
- **API Docs**: http://localhost:8000/docs
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions

## License

MIT License - See LICENSE file

## Contributing

See CONTRIBUTING.md for guidelines
