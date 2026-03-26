import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def to_excel(data, path):
    pd.DataFrame(data).to_excel(path, index=False)

def to_pdf(metrics, path):
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    content = [Paragraph(f"{k}: {v}", styles["Normal"]) for k,v in metrics.items()]
    doc.build(content)