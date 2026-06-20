"""PDF Generation Service for DecisionLens Reports"""
import json
from datetime import datetime
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    PageBreak,
    Image,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT


class PDFReportGenerator:
    """Generate professional PDF reports for decision analysis"""

    def __init__(self):
        self.page_width, self.page_height = letter
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the report"""
        self.styles.add(
            ParagraphStyle(
                name="CustomTitle",
                parent=self.styles["Heading1"],
                fontSize=24,
                textColor=colors.HexColor("#1e40af"),
                spaceAfter=30,
                alignment=TA_CENTER,
            )
        )
        self.styles.add(
            ParagraphStyle(
                name="CustomHeading",
                parent=self.styles["Heading2"],
                fontSize=16,
                textColor=colors.HexColor("#1e40af"),
                spaceAfter=12,
                spaceBefore=12,
            )
        )
        self.styles.add(
            ParagraphStyle(
                name="CustomBody",
                parent=self.styles["BodyText"],
                fontSize=11,
                leading=14,
            )
        )

    def generate_clarity_report(
        self,
        decision_title: str,
        report_data: dict,
        user_name: str = "User",
    ) -> BytesIO:
        """Generate a complete clarity report PDF"""
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=letter,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
        )

        story = []

        # Header
        story.append(
            Paragraph(
                f"DecisionLens AI<br/>Clarity Report",
                self.styles["CustomTitle"],
            )
        )
        story.append(
            Paragraph(
                f"<b>{decision_title}</b>",
                self.styles["Heading2"],
            )
        )
        story.append(
            Paragraph(
                f"Prepared for: {user_name} | Date: {datetime.now().strftime('%B %d, %Y')}",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 0.3 * inch))

        # Executive Summary
        story.append(
            Paragraph(
                "Executive Summary",
                self.styles["CustomHeading"],
            )
        )
        story.append(
            Paragraph(
                report_data.get("executive_summary", ""),
                self.styles["CustomBody"],
            )
        )
        story.append(Spacer(1, 0.2 * inch))

        # Key Insights
        story.append(
            Paragraph(
                "Key Insights",
                self.styles["CustomHeading"],
            )
        )
        for insight in report_data.get("key_insights", []):
            story.append(
                Paragraph(
                    f"• {insight}",
                    self.styles["CustomBody"],
                )
            )
        story.append(Spacer(1, 0.2 * inch))

        # Ranked Priorities
        story.append(
            Paragraph(
                "Ranked Priorities",
                self.styles["CustomHeading"],
            )
        )
        for idx, priority in enumerate(report_data.get("ranked_priorities", []), 1):
            story.append(
                Paragraph(
                    f"{idx}. {priority}",
                    self.styles["CustomBody"],
                )
            )
        story.append(Spacer(1, 0.2 * inch))

        # Core Tradeoffs
        story.append(PageBreak())
        story.append(
            Paragraph(
                "Core Tradeoffs",
                self.styles["CustomHeading"],
            )
        )
        for tradeoff in report_data.get("core_tradeoffs", []):
            story.append(
                Paragraph(
                    f"<b>• {tradeoff.get('description', '')}</b>",
                    self.styles["CustomBody"],
                )
            )
            story.append(
                Paragraph(
                    f"Impact: {tradeoff.get('impact', 'Unknown').upper()}",
                    self.styles["Normal"],
                )
            )
            story.append(Spacer(1, 0.1 * inch))

        # Missing Information
        story.append(Spacer(1, 0.2 * inch))
        story.append(
            Paragraph(
                "Missing Information",
                self.styles["CustomHeading"],
            )
        )
        for info in report_data.get("missing_information", []):
            story.append(
                Paragraph(
                    f"• {info}",
                    self.styles["CustomBody"],
                )
            )
        story.append(Spacer(1, 0.2 * inch))

        # Next Steps
        story.append(PageBreak())
        story.append(
            Paragraph(
                "Next Research Steps",
                self.styles["CustomHeading"],
            )
        )
        for idx, step in enumerate(report_data.get("next_research_steps", []), 1):
            story.append(
                Paragraph(
                    f"{idx}. {step}",
                    self.styles["CustomBody"],
                )
            )
        story.append(Spacer(1, 0.2 * inch))

        # Decision Framework
        story.append(
            Paragraph(
                "Decision Framework",
                self.styles["CustomHeading"],
            )
        )
        story.append(
            Paragraph(
                report_data.get("decision_framework", ""),
                self.styles["CustomBody"],
            )
        )

        # Gut Check Questions
        story.append(Spacer(1, 0.2 * inch))
        story.append(
            Paragraph(
                "Gut Check Questions",
                self.styles["CustomHeading"],
            )
        )
        for question in report_data.get("gut_check_questions", []):
            story.append(
                Paragraph(
                    f"• {question}",
                    self.styles["CustomBody"],
                )
            )

        # Footer
        story.append(Spacer(1, 0.3 * inch))
        story.append(PageBreak())
        story.append(
            Paragraph(
                "<i>This report is a decision aid, not a decision. You are responsible for your final choice.</i>",
                self.styles["Normal"],
            )
        )
        story.append(
            Paragraph(
                "Generated by DecisionLens AI | www.decisionlens.ai",
                self.styles["Normal"],
            )
        )

        doc.build(story)
        pdf_buffer.seek(0)
        return pdf_buffer

    def generate_scenario_comparison_pdf(
        self,
        decision_title: str,
        scenarios: list,
        user_name: str = "User",
    ) -> BytesIO:
        """Generate PDF comparing multiple scenarios"""
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=letter,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
        )

        story = []

        # Header
        story.append(
            Paragraph(
                f"DecisionLens AI<br/>Scenario Analysis",
                self.styles["CustomTitle"],
            )
        )
        story.append(
            Paragraph(
                f"<b>{decision_title}</b>",
                self.styles["Heading2"],
            )
        )
        story.append(Spacer(1, 0.2 * inch))

        # Scenario Details
        for scenario in scenarios:
            story.append(
                Paragraph(
                    f"{scenario.get('name', '')}",
                    self.styles["CustomHeading"],
                )
            )
            story.append(
                Paragraph(
                    f"<b>Description:</b> {scenario.get('description', '')}",
                    self.styles["CustomBody"],
                )
            )
            story.append(Spacer(1, 0.1 * inch))

            # Financial Outcome
            story.append(
                Paragraph(
                    "<b>Financial Outcome:</b>",
                    self.styles["Normal"],
                )
            )
            story.append(
                Paragraph(
                    scenario.get("financial_outcome", ""),
                    self.styles["CustomBody"],
                )
            )
            story.append(Spacer(1, 0.1 * inch))

            # Career Impact
            story.append(
                Paragraph(
                    "<b>Career Impact:</b>",
                    self.styles["Normal"],
                )
            )
            story.append(
                Paragraph(
                    scenario.get("career_impact", ""),
                    self.styles["CustomBody"],
                )
            )
            story.append(Spacer(1, 0.1 * inch))

            # Lifestyle Changes
            story.append(
                Paragraph(
                    "<b>Lifestyle Changes:</b>",
                    self.styles["Normal"],
                )
            )
            story.append(
                Paragraph(
                    scenario.get("lifestyle_changes", ""),
                    self.styles["CustomBody"],
                )
            )
            story.append(Spacer(1, 0.3 * inch))

        doc.build(story)
        pdf_buffer.seek(0)
        return pdf_buffer
