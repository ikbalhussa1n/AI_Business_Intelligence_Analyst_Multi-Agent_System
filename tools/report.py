from langchain.tools import tool
from datetime import datetime
import random


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from langchain.tools import tool


@tool
def create_markdown_report(
    title: str,
    content: str
):
    """
    Creates a markdown report.
    """

    filename = f"report_{datetime.now().timestamp()}_{random.randint(0,100)}.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"# {title}\n\n")
        file.write(content)

    return filename




@tool
def create_pdf_report(
    title: str,
    content: str
):
    """
    Creates a PDF report.
    """

    filename = f"report_{int(datetime.now().timestamp())}_{random.randint(0,100)}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(title, styles["Title"])
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            content.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(elements)

    return filename