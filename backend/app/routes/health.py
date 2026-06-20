"""Health check endpoint"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "DecisionLens AI",
    }


@router.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "DecisionLens AI API",
        "version": "0.1.0",
        "docs": "/docs",
    }
