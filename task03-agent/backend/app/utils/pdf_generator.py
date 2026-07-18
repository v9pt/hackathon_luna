import base64
import html
import io
import logging
import re
from typing import Any, Dict, List, Optional

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    Image,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

logger = logging.getLogger(__name__)


def md_to_html(text: str) -> str:
    """Escapes HTML special characters and translates simple Markdown inline syntax

    to ReportLab paragraph formatting tags (e.g. <b>, <i>, <font>).
    """
    # 1. Escape HTML special characters to avoid syntax conflicts with ReportLab tags
    text = html.escape(text)

    # 2. Convert bold (**text** or __text__)
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"__(.*?)__", r"<b>\1</b>", text)

    # 3. Convert italic (*text* or _text_)
    text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)
    text = re.sub(r"_(.*?)_", r"<i>\1</i>", text)

    # 4. Convert inline code (`code`)
    text = re.sub(
        r"`(.*?)`",
        r'<font face="Courier" color="#c7254e" size="9">\1</font>',
        text,
    )

    return text


def generate_pdf(
    markdown_content: str, charts: Optional[List[Dict[str, Any]]] = None
) -> bytes:
    """Generates a professionally styled PDF from Markdown content and optional charts.

    Args:
        markdown_content: The markdown report text.
        charts: List of dictionaries containing base64 chart data, e.g.:
                [{"name": "market_share.png", "base64": "..."}]

    Returns:
        Bytes containing the generated PDF file.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=54,  # 0.75 inches
        leftMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    styles = getSampleStyleSheet()

    # Define professional typography and color scheme (Navy primary, Cool Grey secondary)
    primary_color = colors.HexColor("#1A365D")
    secondary_color = colors.HexColor("#4A5568")
    text_color = colors.HexColor("#2D3748")
    bg_code_color = colors.HexColor("#F7FAFC")
    border_color = colors.HexColor("#E2E8F0")

    # Update base Normal style
    styles["Normal"].textColor = text_color
    styles["Normal"].fontSize = 10
    styles["Normal"].leading = 14

    # Create professional custom styles
    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=primary_color,
        spaceAfter=15,
        alignment=TA_LEFT,
    )

    h1_style = ParagraphStyle(
        "ReportH1",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=primary_color,
        spaceBefore=15,
        spaceAfter=8,
        keepWithNext=True,
    )

    h2_style = ParagraphStyle(
        "ReportH2",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True,
    )

    bullet_style = ParagraphStyle(
        "ReportBullet",
        parent=styles["Normal"],
        leftIndent=20,
        firstLineIndent=-10,
        spaceAfter=4,
    )

    code_block_style = ParagraphStyle(
        "ReportCodeBlock",
        fontName="Courier",
        fontSize=9,
        leading=11,
        textColor=text_color,
        backColor=bg_code_color,
        borderColor=border_color,
        borderWidth=1,
        borderPadding=6,
        spaceBefore=8,
        spaceAfter=8,
    )

    story: List[Any] = []

    lines = markdown_content.split("\n")
    in_code_block = False
    code_block_lines = []

    for line in lines:
        stripped = line.strip()

        # Handle start/end of preformatted code blocks
        if stripped.startswith("```"):
            if in_code_block:
                # End of code block, flush content
                code_text = "\n".join(code_block_lines)
                escaped_code = html.escape(code_text)
                story.append(
                    Paragraph(f"<pre>{escaped_code}</pre>", code_block_style)
                )
                code_block_lines = []
                in_code_block = False
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_block_lines.append(line)
            continue

        # Handle inline base64 images, e.g. ![Chart](data:image/png;base64,iVBORw...)
        img_match = re.search(
            r"!\[(.*?)\]\(data:image\/(png|jpeg|jpg);base64,([A-Za-z0-9+/=\s\n\r]+)\)",
            line,
        )
        if img_match:
            title = img_match.group(1)
            base64_data = img_match.group(3).strip()
            try:
                img_data = base64.b64decode(base64_data)
                img_buf = io.BytesIO(img_data)
                img = Image(img_buf, width=450, height=280)

                chart_table = Table([[img]], colWidths=[450])
                chart_table.setStyle(
                    TableStyle(
                        [
                            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                        ]
                    )
                )

                story.append(
                    KeepTogether(
                        [
                            Paragraph(md_to_html(title or "Visualization"), h2_style),
                            chart_table,
                            Spacer(1, 10),
                        ]
                    )
                )
            except Exception as e:
                logger.error("Failed to decode inline base64 image in PDF: %s", e)
            continue

        # Handle header elements
        if stripped.startswith("# "):
            story.append(Paragraph(md_to_html(stripped[2:]), title_style))
            story.append(Spacer(1, 10))
        elif stripped.startswith("## "):
            story.append(Paragraph(md_to_html(stripped[3:]), h1_style))
        elif stripped.startswith("### "):
            story.append(Paragraph(md_to_html(stripped[4:]), h2_style))

        # Handle list elements
        elif stripped.startswith("- ") or stripped.startswith("* "):
            bullet_text = md_to_html(stripped[2:])
            story.append(Paragraph(f"&bull; {bullet_text}", bullet_style))
        elif re.match(r"^\d+\.\s", stripped):
            match = re.match(r"^(\d+)\.\s(.*)", stripped)
            if match:
                num = match.group(1)
                item_text = md_to_html(match.group(2))
                story.append(Paragraph(f"{num}. {item_text}", bullet_style))

        # Handle normal text paragraphs
        elif stripped:
            para_text = md_to_html(line)
            story.append(Paragraph(para_text, styles["Normal"]))
            story.append(Spacer(1, 6))
        else:
            story.append(Spacer(1, 6))

    # Append visualizations section if charts are provided
    if charts:
        story.append(Spacer(1, 15))
        story.append(Paragraph("Visualizations", h1_style))
        story.append(Spacer(1, 10))

        for chart in charts:
            try:
                img_data = base64.b64decode(chart["base64"])
                img_buf = io.BytesIO(img_data)
                img = Image(img_buf, width=450, height=280)

                chart_table = Table([[img]], colWidths=[450])
                chart_table.setStyle(
                    TableStyle(
                        [
                            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                        ]
                    )
                )

                story.append(
                    KeepTogether(
                        [
                            Paragraph(
                                md_to_html(chart.get("name", "Chart")), h2_style
                            ),
                            chart_table,
                            Spacer(1, 10),
                        ]
                    )
                )
            except Exception as e:
                logger.error(
                    "Failed to embed chart %s in PDF: %s",
                    chart.get("name"),
                    e,
                )

    doc.build(story)
    return buffer.getvalue()
