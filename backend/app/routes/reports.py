"""Routes for report generation and export"""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.services.pdf_service import PDFService
from io import BytesIO

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/decision/{decision_id}")
async def get_decision_report(
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Get clarity report for decision"""
    # This would fetch the report from DB
    return {
        "decision_id": decision_id,
        "message": "Report retrieval implemented in Phase 9"
    }


@router.post("/decision/{decision_id}/export-pdf")
async def export_report_pdf(
    decision_id: str,
    db: Session = Depends(get_db)
):
    """Export clarity report as PDF"""
    
    # Mock report data for now
    report_data = {
        "decision_title": "Major Life Decision",
        "key_insights": [
            "Multiple paths have merit",
            "Your values should guide decision",
            "Uncertainty is normal and expected"
        ],
        "ranked_priorities": [
            "Personal fulfillment",
            "Financial sustainability",
            "Career growth"
        ],
        "core_tradeoffs": [
            "Stability vs Growth",
            "Income vs Fulfillment",
            "Security vs Opportunity"
        ],
        "missing_information": [
            "Detailed company culture info",
            "Long-term market trends",
            "Personal satisfaction factors"
        ],
        "next_research_steps": [
            "Interview people in each path",
            "Research company/program details",
            "Map your decision criteria"
        ],
        "decision_framework": "Consider values first, then financial feasibility, then personal excitement.",
        "gut_check_questions": [
            "Which path excites you most?",
            "What would you regret not trying?",
            "What are you truly afraid of?"
        ]
    }
    
    # Generate PDF
    pdf_buffer = PDFService.generate_clarity_report_pdf(report_data)
    
    return StreamingResponse(
        iter([pdf_buffer.getvalue()]),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=clarity_report_{decision_id}.pdf"}
    )
