from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(topics, content, filename='output.pdf'):
    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Define a new style for left-aligned topics with bullets
    topic_style = ParagraphStyle(name='TopicStyle', parent=styles['Title'])
    topic_style.alignment = 0  # 0 = Left

    # Create a list to hold the paragraphs
    elements = []

    # Loop through each topic and content pair
    for topic, cont in zip(topics, content):
        # Add topic with bullet and content as paragraphs
        bullet = "&#8226;"  # Unicode for bullet symbol
        topic_with_bullet = f"<bullet>{bullet}</bullet> {topic}"
        elements.append(Paragraph(topic_with_bullet, topic_style))
        elements.append(Paragraph(cont, styles['Normal']))
        # Add some space between topics
        elements.append(Paragraph("<br/><br/>", styles['Normal']))

    # Build the PDF document
    doc.build(elements)

# Example usage
topics = ["Topic 1", "Topic 2", "Topic 3"]
content = [
    "Content of Topic 1",
    "Content of Topic 2",
    "Content of Topic 3"
]

def run(topics, content):
    generate_pdf(topics, content, filename='multiple_topics_with_bullets.pdf')
    print('success')
