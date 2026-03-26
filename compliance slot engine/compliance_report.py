from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate(metrics, path="compliance_report.pdf"):
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    content = [Paragraph(f"{k}: {v}", styles["Normal"]) for k,v in metrics.items()]
    doc.build(content)