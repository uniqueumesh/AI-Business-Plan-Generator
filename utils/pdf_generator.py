"""
PDF generation utilities using ReportLab.

Converts simple Markdown-like content into a readable PDF without external binaries.
"""
from io import BytesIO
from typing import List
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import inch


def _split_lines(text: str) -> List[str]:
    return [line.rstrip() for line in text.splitlines()]


def generate_pdf(markdown_text: str, company_name: str) -> bytes:
    """Generate a PDF document from markdown-like text.

    Args:
        markdown_text: The business plan content (Markdown-like) to render.
        company_name: Company name for the title header.

    Returns:
        PDF bytes suitable for sending to a download button.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=LETTER,
        leftMargin=0.8 * inch,
        rightMargin=0.8 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.8 * inch,
        title=f"{company_name} Business Plan",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name="TitleCenter",
        parent=styles["Title"],
        alignment=TA_CENTER,
        spaceAfter=12,
    )
    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    story = []
    # Title
    story.append(Paragraph(f"{company_name} — Business Plan", title_style))
    story.append(Spacer(1, 0.2 * inch))

    lines = _split_lines(markdown_text)

    bullet_buffer: List[str] = []

    def flush_bullets():
        if not bullet_buffer:
            return
        items = [ListItem(Paragraph(item, normal_style)) for item in bullet_buffer]
        story.append(ListFlowable(items, bulletType="bullet"))
        story.append(Spacer(1, 6))
        bullet_buffer.clear()

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_bullets()
            story.append(Spacer(1, 6))
            continue

        # Detect headings: numeric enumerated headings like "1. Executive Summary"
        if line[:2].isdigit() or (len(line) > 2 and line[0].isdigit() and line[1] == "."):
            flush_bullets()
            story.append(Paragraph(line, heading_style))
            story.append(Spacer(1, 4))
            continue

        # Detect bullets starting with '-', '*', '•'
        if line.startswith("- ") or line.startswith("* ") or line.startswith("• "):
            bullet_buffer.append(line[2:].strip())
            continue

        # Bold markers cleanup for simple readability
        clean = line.replace("**", "").replace("__", "")

        flush_bullets()
        story.append(Paragraph(clean, normal_style))

    flush_bullets()

    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes


