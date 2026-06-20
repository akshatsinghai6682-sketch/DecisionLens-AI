"""PDF Service - Generate reports and PDFs"""

from typing import Dict, Any
from app.services.report_service import ReportService


class PDFService:
    """Service for PDF generation and management"""

    @staticmethod
    def generate_clarity_report_pdf(report_data: Dict[str, Any]):
        """Generate PDF clarity report"""
        return ReportService.generate_pdf_report(report_data)
