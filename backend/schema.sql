-- Create DecisionLens AI database schema

CREATE DATABASE IF NOT EXISTS decisionlens;
USE decisionlens;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    INDEX idx_email (email),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Decisions table
CREATE TABLE IF NOT EXISTS decisions (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    title VARCHAR(500) NOT NULL,
    description LONGTEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'in_progress',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    resolved_at DATETIME NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at),
    INDEX idx_title (title)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Decision contexts table
CREATE TABLE IF NOT EXISTS decision_contexts (
    id VARCHAR(36) PRIMARY KEY,
    decision_id VARCHAR(36) UNIQUE NOT NULL,
    values_profile JSON DEFAULT '{}',
    constraints JSON DEFAULT '{}',
    timeline VARCHAR(255),
    financial_situation VARCHAR(255),
    risk_tolerance VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (decision_id) REFERENCES decisions(id) ON DELETE CASCADE,
    INDEX idx_decision_id (decision_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Scenarios table
CREATE TABLE IF NOT EXISTS scenarios (
    id VARCHAR(36) PRIMARY KEY,
    decision_id VARCHAR(36) NOT NULL,
    label VARCHAR(255) NOT NULL,
    narrative LONGTEXT NOT NULL,
    financial_score FLOAT NOT NULL,
    career_score FLOAT NOT NULL,
    lifestyle_score FLOAT NOT NULL,
    risk_score FLOAT NOT NULL,
    values_score FLOAT NOT NULL,
    confidence_level FLOAT DEFAULT 0.7,
    assumptions JSON DEFAULT '{}',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (decision_id) REFERENCES decisions(id) ON DELETE CASCADE,
    INDEX idx_decision_id (decision_id),
    INDEX idx_label (label)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Advisor perspectives table
CREATE TABLE IF NOT EXISTS advisor_perspectives (
    id VARCHAR(36) PRIMARY KEY,
    scenario_id VARCHAR(36) NOT NULL,
    advisor_type VARCHAR(255) NOT NULL,
    key_concern LONGTEXT NOT NULL,
    recommendation LONGTEXT NOT NULL,
    blind_spot_identified LONGTEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(id) ON DELETE CASCADE,
    INDEX idx_scenario_id (scenario_id),
    INDEX idx_advisor_type (advisor_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tradeoffs table
CREATE TABLE IF NOT EXISTS tradeoffs (
    id VARCHAR(36) PRIMARY KEY,
    decision_id VARCHAR(36) NOT NULL,
    description LONGTEXT NOT NULL,
    category VARCHAR(255) NOT NULL,
    surfaced_by VARCHAR(255),
    acknowledged BOOLEAN DEFAULT FALSE,
    user_notes LONGTEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (decision_id) REFERENCES decisions(id) ON DELETE CASCADE,
    INDEX idx_decision_id (decision_id),
    INDEX idx_category (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Sessions table
CREATE TABLE IF NOT EXISTS sessions (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    decision_id VARCHAR(36) NOT NULL,
    messages JSON DEFAULT '[]',
    phase VARCHAR(255),
    current_question_index VARCHAR(10) DEFAULT '0',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (decision_id) REFERENCES decisions(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_decision_id (decision_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create indexes for performance
CREATE INDEX idx_decisions_user_created ON decisions(user_id, created_at);
CREATE INDEX idx_sessions_user_decision ON sessions(user_id, decision_id);
CREATE INDEX idx_scenarios_decision ON scenarios(decision_id);
