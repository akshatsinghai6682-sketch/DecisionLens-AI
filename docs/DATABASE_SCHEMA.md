# DecisionLens AI - Database Schema

## Tables Overview

### users
Stores user information (mock authentication).

```sql
id: VARCHAR(36) - UUID primary key
email: VARCHAR(255) - User email (unique)
name: VARCHAR(255) - User name
created_at: DATETIME - Account creation timestamp
updated_at: DATETIME - Last update timestamp
is_active: BOOLEAN - Account status
```

### decisions
Main decision records.

```sql
id: VARCHAR(36) - UUID primary key
user_id: VARCHAR(36) - Foreign key to users
title: VARCHAR(500) - Decision title
description: LONGTEXT - Detailed description
status: VARCHAR(50) - in_progress|completed|archived
created_at: DATETIME - Creation timestamp
updated_at: DATETIME - Last update timestamp
resolved_at: DATETIME - When decision was made (nullable)
```

### decision_contexts
User profile and constraints for a decision.

```sql
id: VARCHAR(36) - UUID primary key
decision_id: VARCHAR(36) - Foreign key to decisions (unique)
values_profile: JSON - Top 3-5 values {"value": "importance"}
constraints: JSON - Geographic, family, financial constraints
timeline: VARCHAR(255) - short_term|medium_term|long_term
financial_situation: VARCHAR(255) - Financial constraints
risk_tolerance: VARCHAR(255) - low|medium|high
created_at: DATETIME - Creation timestamp
updated_at: DATETIME - Last update timestamp
```

### scenarios
Simulation results for different decision paths.

```sql
id: VARCHAR(36) - UUID primary key
decision_id: VARCHAR(36) - Foreign key to decisions
label: VARCHAR(255) - "Best Case"|"Expected Case"|"Worst Case"
narrative: LONGTEXT - Detailed scenario description
financial_score: FLOAT - 0-100
career_score: FLOAT - 0-100
lifestyle_score: FLOAT - 0-100
risk_score: FLOAT - 0-100 (higher = more risk)
values_score: FLOAT - 0-100 (alignment with values)
confidence_level: FLOAT - 0-1 (AI confidence in scenario)
assumptions: JSON - {"assumption": "value"}
created_at: DATETIME - Creation timestamp
```

### advisor_perspectives
Perspectives from 5 advisor archetypes for each scenario.

```sql
id: VARCHAR(36) - UUID primary key
scenario_id: VARCHAR(36) - Foreign key to scenarios
advisor_type: VARCHAR(255) - "Parent"|"Entrepreneur"|"Academic"|"Counselor"|"Analyst"
key_concern: LONGTEXT - Main concern from this perspective
recommendation: LONGTEXT - Recommendation from this advisor
blind_spot_identified: LONGTEXT - Blind spot identified by advisor
created_at: DATETIME - Creation timestamp
```

### tradeoffs
Hidden tradeoffs identified in the decision.

```sql
id: VARCHAR(36) - UUID primary key
decision_id: VARCHAR(36) - Foreign key to decisions
description: LONGTEXT - Tradeoff description
category: VARCHAR(255) - "Opportunity Cost"|"Geographic"|"Financial"|etc
surfaced_by: VARCHAR(255) - Agent that identified this tradeoff
acknowledged: BOOLEAN - User acknowledged this tradeoff
user_notes: LONGTEXT - User's notes on tradeoff (nullable)
created_at: DATETIME - Creation timestamp
```

### sessions
Conversation sessions tracking.

```sql
id: VARCHAR(36) - UUID primary key
user_id: VARCHAR(36) - Foreign key to users
decision_id: VARCHAR(36) - Foreign key to decisions
messages: JSON - [{"role": "user|assistant", "content": "...", "timestamp": "..."}, ...]
phase: VARCHAR(255) - diagnostic|tradeoff_review|simulation|perspective|uncertainty|report
current_question_index: VARCHAR(10) - Current question number in phase
created_at: DATETIME - Session start timestamp
updated_at: DATETIME - Last activity timestamp
```

## Key Relationships

```
users (1) ──→ (many) decisions
users (1) ──→ (many) sessions

decisions (1) ──→ (1) decision_contexts
decisions (1) ──→ (many) scenarios
decisions (1) ──→ (many) tradeoffs
decisions (1) ──→ (many) sessions

scenarios (1) ──→ (many) advisor_perspectives
```

## Indexes for Performance

- users: email, created_at
- decisions: user_id, status, created_at, title
- scenarios: decision_id, label
- advisor_perspectives: scenario_id, advisor_type
- tradeoffs: decision_id, category
- sessions: user_id, decision_id, created_at
- Composite: decisions(user_id, created_at), sessions(user_id, decision_id)

## Data Types & Constraints

- UUIDs (36 chars) for all primary keys
- UTF8MB4 charset for emoji/special character support
- JSON columns for flexible, schema-less data
- CASCADE delete for referential integrity
- NOT NULL constraints on required fields
- Index on frequently queried columns
