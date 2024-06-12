from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_pdf(topics, content, filename='output.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    topic_style = ParagraphStyle(name='TopicStyle', parent=styles['Title'])
    topic_style.alignment = 0
    elements = []
    for topic, cont in zip(topics, content):
        bullet = "&#8226;"
        topic_with_bullet = f"<bullet>{bullet}</bullet> {topic}"
        elements.append(Paragraph(topic_with_bullet, topic_style))
        elements.append(Paragraph(cont, styles['Normal']))
        elements.append(Paragraph("<br/><br/>", styles['Normal']))

    doc.build(elements)

def run(topics, content):
    generate_pdf(topics, content, filename='Specialised notes.pdf')