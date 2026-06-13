from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(text, file_path):
    """
    Export deck analysis to PDF.

    Parameters:
        text (str): Report text
        file_path (str): Location where PDF will be saved
    """

    pdf = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        if line.strip() == "":
            story.append(Spacer(1, 6))
            continue

        story.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 3)
        )

    pdf.build(story)