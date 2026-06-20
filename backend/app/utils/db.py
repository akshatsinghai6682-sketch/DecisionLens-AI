"""Database utilities and session management"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool
from app.config import settings
import logging

logger = logging.getLogger(__name__)

# Create engine with connection pooling
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    poolclass=QueuePool,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,  # Verify connections before using
    connect_args={"charset": "utf8mb4"},
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Session:
    """Get database session for dependency injection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database tables"""
    try:
        from app.models import Base
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise


def get_engine():
    """Get SQLAlchemy engine"""
    return engine
